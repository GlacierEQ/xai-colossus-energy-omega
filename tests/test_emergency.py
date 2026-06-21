# SPDX-License-Identifier: Proprietary
# Copyright (c) 2026 Casey del Carpio Barton
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from megapack_controller import MegapackController, MegapackState
def test_emergency():
    ctrl = MegapackController()
    ctrl.trip_breaker_on_fault(45.0)
    assert ctrl.state == MegapackState.FAULT
    print("  [PASS] Emergency earth leakage breaker tripping sequence validated.")
