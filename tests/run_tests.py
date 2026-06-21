# SPDX-License-Identifier: Proprietary
# Copyright (c) 2026 Casey del Carpio Barton / GlacierEQ — All Rights Reserved
import os
import sys
import time

# Ensure parent directory is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from megapack_controller import MegapackController, MegapackState

def test_megapack_fsm():
    print("[TEST] Running Tesla Megapack dispatch state machine...")
    t0 = time.perf_counter()
    
    controller = MegapackController()
    assert controller.precharge_bus_bars() == True
    
    # Run predictive warmup
    controller.run_predictive_power_boost("08:50")
    assert controller.state == MegapackState.DISCHARGING
    print("  - Verified Megapack predictive grid-buffer discharge state")
    
    # Peak pricing dispatch check
    state = controller.update_state(80.0, 280.0, 15.0)
    assert state == MegapackState.DISCHARGING
    print("  - Verified peak-shaving dispatch triggering at $280/MWh")
    
    duration_ms = (time.perf_counter() - t0) * 1000.0
    print(f"[TEST-METRICS] Status=SUCCESS Latency={duration_ms:.3f}ms")

if __name__ == '__main__':
    test_megapack_fsm()
