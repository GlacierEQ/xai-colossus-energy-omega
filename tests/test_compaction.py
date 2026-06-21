# SPDX-License-Identifier: Proprietary
# Copyright (c) 2026 Casey del Carpio Barton
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from megapack_controller import MegapackController
def test_compaction():
    ctrl = MegapackController()
    for _ in range(5):
        ctrl.run_dynamic_lumped_log(50.0)
    assert ctrl.nominal_lump_count == 5
    print("  [PASS] Log compaction: 5 nominal battery state checks lumped successfully.")
