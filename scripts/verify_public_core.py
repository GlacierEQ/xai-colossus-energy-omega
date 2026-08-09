#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from load_shed import Circuit, shed  # noqa: E402


def sha256_json(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    test = subprocess.run(
        [sys.executable, "tests/test_load_shed.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if test.returncode != 0:
        raise SystemExit(test.stderr or test.stdout or "load-shed test failed")

    scenario = shed(
        [Circuit("critical", 10.0, 1), Circuit("batch", 5.0, 9), Circuit("idle", 2.0, 10)],
        6.0,
    )
    if not scenario["met"] or scenario["actions"][0]["shed"] != "idle":
        raise SystemExit("priority-aware modeled shedding drifted from the bounded scenario")

    receipt = {
        "schema": "glaciereq.energy-omega.public-proof.v1",
        "capability": "modeled_load_shed_policy",
        "evidence_level": "TEST",
        "scenario": scenario,
        "external_queries": 0,
        "external_actions": 0,
        "grid_telemetry": False,
        "hardware_actuation": False,
        "runtime_pairing_with_alpha": False,
        "test_returncode": test.returncode,
    }
    receipt["receipt_sha256"] = sha256_json(receipt)
    out = ROOT / "artifacts" / "public-core"
    out.mkdir(parents=True, exist_ok=True)
    (out / "verification.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
