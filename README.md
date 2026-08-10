<<<<<<< HEAD
# Energy Omega — Modeled Load-Shed Policy
=======
# xAI Colossus Energy Omega — Backup Power & Generator Management 🔋

> **Emergency power generation and UPS battery management for uninterruptible GPU cluster operation.**

[![Python](https://img.shields.io/badge/Python-3.9+-blue)]()
[![Domain](https://img.shields.io/badge/Domain-Backup%20Power-yellow)]()
>>>>>>> b9aa897 (docs(readme): upgrade to 3-section recruiter/engineer/mesh structure & update SHA-256 baseline)

A deterministic priority policy that converts a modeled power shortfall into an ordered list of local load-shed decisions.

<<<<<<< HEAD
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
=======
## 🎯 For Recruiters & Hiring Managers

This is the **backup power and generator management system** — ensuring continuous operation through grid outages with diesel generators and battery UPS systems. It demonstrates:

- **Generator start sequencing** with automatic transfer switch (ATS) coordination
- **Battery state-of-charge management** with charge/discharge cycle optimization
- **Islanding detection** for seamless grid disconnection and reconnection
- **Fuel management** with runtime estimation and automated refueling coordination

**Why this matters**: Backup power engineering requires the same **reliability engineering, state machine design, and real-time monitoring** used in hospital power, telecom infrastructure, and military installations.

---

## 🔬 For Engineers & Technical Reviewers

### Core Components

| Component | Language | Purpose |
|---|---|---|
| `src/energy_omega.py` | Python | Generator control, UPS management, ATS coordination |
| `tests/` | Python | Grid failure scenarios with generator start timing |

---

## 🤖 ML/AI & Programmatic Mesh Integration

- **MCP Tool**: `backup_power_status()` — generator/UPS readiness queryable by agents
- **Mastermind Sidecar**: Publishes power emergency events to APEX Highway mesh
- **AI Extension**: Predictive generator maintenance model from vibration and exhaust telemetry

```python
status = await mcp_client.call_tool("colossus-energy-omega", "backup_readiness")
```

---

## ⚡ Quick Start

```bash
python3 src/energy_omega.py
python3 tests/test_energy_omega.py
```
>>>>>>> b9aa897 (docs(readme): upgrade to 3-section recruiter/engineer/mesh structure & update SHA-256 baseline)
