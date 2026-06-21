# SPDX-License-Identifier: Proprietary
# Copyright (c) 2026 Casey del Carpio Barton
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from megapack_controller import MegapackController, MegapackState
def test_nominal():
    ctrl = MegapackController()
    assert ctrl.precharge_bus_bars() == True
    state = ctrl.update_state(40.0, 45.0, 10.0)
    assert state == MegapackState.CHARGING
    print("  [PASS] Nominal battery charge utility cycles successful.")
