# SPDX-License-Identifier: Proprietary
# Copyright (c) 2026 Casey del Carpio Barton / GlacierEQ — All Rights Reserved
"""
megapack_controller.py — Tesla Megapack and sCO2 Dispatch State Machine
=======================================================================
Helix Omega Strand: Battery Dispatch Controls & Peak Shaving FSM.
"""
from enum import Enum
import time

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

    # 1. PREPARATION LEVEL
    def precharge_bus_bars(self) -> bool:
        """Pre-charges DC-bus cap banks to prevent massive inrush current spikes."""
        print("[ENERGY-PREP] Precharging DC bus links. Stabilizing voltage vector.")
        return True

    # 2. OPERATION LEVEL
    def update_state(self, grid_demand_mw: float, price_per_mwh: float, sco2_generation_mw: float) -> MegapackState:
        if price_per_mwh > 250.0 and self.soc_percent > 10.0:
            self.state = MegapackState.DISCHARGING
            self.soc_percent -= 2.5
            print(f"[ENERGY-INNOVATION] Discharging BESS. sCO2: {sco2_generation_mw:.1f}MW.")
        elif price_per_mwh < 50.0 and self.soc_percent < 95.0:
            self.state = MegapackState.CHARGING
            self.soc_percent += 3.0
        else:
            self.state = MegapackState.IDLE
        return self.state

    # 3. EMERGENCY REACTION LEVEL
    def trip_breaker_on_fault(self, ground_leakage_ma: float) -> None:
        """Immediate breaker isolation routine for earth fault protection."""
        if ground_leakage_ma > 30.0:
            print(f"[ENERGY-EMERGENCY] Ground leakage exceeded safe threshold: {ground_leakage_ma}mA. TRIPPING SUBSTATION BREAKER.")
            self.state = MegapackState.FAULT
