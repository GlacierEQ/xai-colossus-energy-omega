# SPDX-License-Identifier: Proprietary
# Copyright (c) 2026 Casey del Carpio Barton / GlacierEQ — All Rights Reserved
"""
megapack_controller.py — Tesla Megapack and sCO2 Dispatch State Machine
=======================================================================
Helix Omega Strand: Battery Dispatch Controls & Peak Shaving FSM.
"""
from enum import Enum
import time
import json
import os

class MegapackState(Enum):
    IDLE = 1
    CHARGING = 2
    DISCHARGING = 3
    FAULT = 4

class MegapackController:
    def __init__(self, capacity_mwh: float = 100.0) -> None:
        self.capacity_mwh = capacity_mwh
        self.soc_percent = 50.0
        self.state = MegapackState.IDLE
        self.memory_file = ".shadow_memory.json"
        self.shadow_recovery_file = ".shadow_recovery"
        
        self.history = self._load_shadow_memory()
        self.nominal_lump_count = 0

    def _load_shadow_memory(self) -> dict:
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r") as f:
                    return json.load(f)
            except Exception:
                pass
        return {"avg_soc": 50.0, "samples": 1}

    def _save_shadow_memory(self) -> None:
        with open(self.memory_file, "w") as f:
            json.dump(self.history, f)

    # 1. PREPARATION LEVEL
    def precharge_bus_bars(self) -> bool:
        print("[ENERGY-PREP] Precharging DC bus links.")
        return True

    # 2. OPERATION LEVEL
    def run_dynamic_lumped_log(self, soc: float) -> None:
        mean_soc = self.history.get("avg_soc", 50.0)
        if abs(soc - mean_soc) <= 1.0:
            self.nominal_lump_count += 1
        else:
            if self.nominal_lump_count > 0:
                print(f"[ENERGY-INFO] (LUMPED {self.nominal_lump_count} nominal battery state-of-charge checks)")
                self.nominal_lump_count = 0
            print(f"[ENERGY-ANOMALY] State of charge variation: {soc:.1f}%")
            
        total_samples = self.history.get("samples", 1) + 1
        self.history["avg_soc"] = ((mean_soc * self.history.get("samples", 1)) + soc) / total_samples
        self.history["samples"] = total_samples
        self._save_shadow_memory()

    def run_predictive_power_boost(self, current_time_str: str) -> None:
        if current_time_str == "08:50":
            print("[ENERGY-INNOVATION] Spooling Megapacks for grid load buffering.")
            self.state = MegapackState.DISCHARGING
            self.soc_percent -= 1.0

    def update_state(self, grid_demand_mw: float, price_per_mwh: float, sco2_generation_mw: float) -> MegapackState:
        # Check shadow override
        if os.path.exists(self.shadow_recovery_file):
            print("[ENERGY-SHADOW] Out-of-band shadow override: Tripping safe system bypass.")
            self.state = MegapackState.IDLE
            return self.state

        self.run_dynamic_lumped_log(self.soc_percent)
        if price_per_mwh > 250.0 and self.soc_percent > 10.0:
            self.state = MegapackState.DISCHARGING
            self.soc_percent -= 2.5
        elif price_per_mwh < 50.0 and self.soc_percent < 95.0:
            self.state = MegapackState.CHARGING
            self.soc_percent += 3.0
        else:
            self.state = MegapackState.IDLE
        return self.state

    # 3. EMERGENCY REACTION LEVEL
    def trip_breaker_on_fault(self, ground_leakage_ma: float) -> None:
        if ground_leakage_ma > 30.0:
            print(f"[ENERGY-EMERGENCY] Ground leakage: {ground_leakage_ma}mA. TRIPPING SUBSTATION BREAKER.")
            self.state = MegapackState.FAULT
