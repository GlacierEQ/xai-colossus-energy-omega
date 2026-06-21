# SPDX-License-Identifier: Proprietary
# Copyright (c) 2026 Casey del Carpio Barton / GlacierEQ — All Rights Reserved
"""
megapack_controller.py — Tesla Megapack and sCO2 Dispatch State Machine
=======================================================================
Helix Omega Strand: Battery Dispatch Controls & Peak Shaving FSM.

INNOVATION: Dynamic switching between sCO2 generator output, battery cells, and TVA grid limits.
"""
from enum import Enum

class MegapackState(Enum):
    IDLE = 1
    CHARGING = 2
    DISCHARGING = 3
    FAULT = 4

class MegapackController:
    """Finite State Machine directing Megapack charging and peak-shaving dispatch."""
    def __init__(self, capacity_mwh: float = 100.0) -> None:
        self.capacity_mwh = capacity_mwh
        self.soc_percent = 50.0  # State of Charge
        self.state = MegapackState.IDLE

    def update_state(self, grid_demand_mw: float, price_per_mwh: float, sco2_generation_mw: float) -> MegapackState:
        # High demand / expensive grid pricing => Discharge Megapack and maximize sCO2 output
        combined_available_mw = (self.soc_percent * 2.0) + sco2_generation_mw
        
        if price_per_mwh > 250.0 and self.soc_percent > 10.0:
            self.state = MegapackState.DISCHARGING
            self.soc_percent -= 2.5
            print(f"[ENERGY-INNOVATION] Discharging BESS and injecting {sco2_generation_mw:.1f}MW sCO2 waste energy.")
        # Low demand / cheap grid pricing => Recharge
        elif price_per_mwh < 50.0 and self.soc_percent < 95.0:
            self.state = MegapackState.CHARGING
            self.soc_percent += 3.0
        else:
            self.state = MegapackState.IDLE
            
        print(f"[ENERGY-INFO] Megapack state changed to {self.state.name}. SoC: {self.soc_percent:.1f}%")
        return self.state
