# Energy Omega — Modeled Load-Shed Policy

A deterministic priority policy that converts a modeled power shortfall into an ordered list of local load-shed decisions.

> **Independent portfolio project.** This repository is not affiliated with, endorsed by, employed by, or deployed at xAI. It does not claim proprietary Colossus data, facility access, grid telemetry, or physical switching authority.

## Recruiter view

The canonical public implementation is [`src/load_shed.py`](src/load_shed.py). Given caller-supplied circuits and a modeled amount of MW that must be freed, it sorts lower-priority loads first and returns a deterministic proposed shedding sequence.

Current verified behavior:

- orders modeled circuits by declared shed priority and MW;
- accumulates proposed removals until the modeled target is met or candidates are exhausted;
- reports the proposed actions, modeled MW freed, and whether the target was met;
- performs no grid query, telemetry read, breaker command, or external action.

The returned `actions` array is a **modeled decision record**, not physical actuation.

## Canonical proof paths

| Path | Role |
|---|---|
| `src/load_shed.py` | deterministic priority-aware shedding policy |
| `tests/test_load_shed.py` | ordering and target-satisfaction check |
| `scripts/verify_public_core.py` | receipt-producing public verifier |
| `.github/workflows/ci.yml` | exact-branch Python truth gate |

Older experimental and integration-oriented files remain preserved but are not automatically promoted by this contract.

## Alpha / Omega relationship

Omega is architecturally paired with [`xai-colossus-energy-alpha`](https://github.com/GlacierEQ/xai-colossus-energy-alpha). Alpha computes modeled budget evidence; Omega proposes a bounded shedding sequence. No live cross-repository runtime, grid connection, facility telemetry stream, or hardware-control path is claimed.

## Verify

```bash
python tests/test_load_shed.py
python scripts/verify_public_core.py
```

## Machine contract

```yaml
schema: glaciereq.component-surface.v1
repository: GlacierEQ/xai-colossus-energy-omega
canonical_branch: master
role: SPECIALIST_COMPONENT
capability: modeled_load_shed_policy
evidence_level: TEST
external_queries: 0
external_actions: 0
grid_telemetry: false
hardware_actuation: false
runtime_pairing_with_alpha: false
company_affiliation_claim: false
```

## Nonclaims

This repository does not establish xAI affiliation, proprietary access, production deployment, live grid/facility telemetry, breaker or power-distribution actuation, measured savings or reliability improvement, validation at a specific MW/GPU/rack scale, or physical-system safety certification.
