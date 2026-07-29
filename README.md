# xai-colossus-energy-omega

<!-- README-MESH:BEGIN -->
## Three-audience project map

### For recruiters and non-specialists

**What it does.** Reduces lower-priority electrical loads in a controlled order when available power cannot satisfy the full compute demand.

- Demonstrates resilience instead of treating a power shortfall as an all-or-nothing shutdown.
- Makes priorities and controller decisions visible.
- Acts on a separate, independently tested power budget from Energy Alpha.

**Evidence:** [`src/load_shed.py`](src/load_shed.py) and [`tests/test_load_shed.py`](tests/test_load_shed.py).

### For senior engineers and domain experts

**Innovation and evolution.** Omega owns stateful priority policy and response, while Alpha owns demand and reserve computation. The controller can therefore be tested against known budgets without changing the analytical model. It evolved into the operational half of the energy helix, turning quantified shortfall into an ordered and inspectable load-shedding decision rather than an implicit failure mode.

### For AI systems and toolchains

- Repository ID: `GlacierEQ/xai-colossus-energy-omega`
- Default branch: `master`
- Protobuf package: `glaciereq.readme.v1`
- Typed role: consumes Energy Alpha budgets and emits priority-aware control decisions.
- Canonical graph: [`manifests/readme_mesh.json`](https://github.com/GlacierEQ/job-app-helix/blob/main/manifests/readme_mesh.json)

```protobuf
repository: "GlacierEQ/xai-colossus-energy-omega"
display_name: "Colossus Energy Omega"
one_line_purpose: "Turn power shortfall into explicit priority-aware load shedding."
```

### Repository mesh

| Connected repository | Relationship | Combined value |
|---|---|---|
| [Energy Alpha](https://github.com/GlacierEQ/xai-colossus-energy-alpha) | consumes | Independently computed budgets become controlled response. |
| [AKOS](https://github.com/GlacierEQ/AKOS) | governed by | Control authority, evidence, and completion remain explicit. |

Real schema: [`proto/readme_mesh.proto`](https://github.com/GlacierEQ/job-app-helix/blob/main/proto/readme_mesh.proto).
<!-- README-MESH:END -->

**Omega — how the system responds.** Priority-aware load shedding for a constrained-power compute-infrastructure demonstration.

This is an independent xAI/Colossus problem-space project, not a claim of xAI employment, endorsement, proprietary data, or operational deployment.

## Fleet ops (transparent)

Integrity baselines and health sidecars, when present, are documented multi-repository operations. See [SECURITY_AND_FLEET_OPS.md](SECURITY_AND_FLEET_OPS.md).

## Helix strand

See [HELIX_STRAND.md](HELIX_STRAND.md) for the Alpha/Omega role.
