# PRAXIS Engine

PRAXIS is a multi-layer probabilistic risk, Bayesian update, and lifecycle reliability engine for modeling cascading infrastructure failures. A scenario file describes systems, domains, stressors, and their dependencies; the engine propagates risk across those layers and produces structured outputs — domain risk scores, failure modes, cascading effects, and lifecycle reliability metrics.

This repository is the **public interface**: the CLI runner, the scenario format, and the documentation. The numerical core (`praxis_core`) is a separately distributed, licensed Python package and is not included here.

## Quick Start

Run a scenario through the CLI runner:

```
python praxis_runner.py scenarios/example_blackswan_saturday.yaml
```

Without the private core installed, the runner prints a notice and exits — the scenario format, runner interface, and documentation remain fully inspectable. With a licensed `praxis_core` wheel installed, the same command executes the scenario against the real engine.

To install the core engine wheel, see [INSTALL_CORE.md](INSTALL_CORE.md).

## Repository Contents

- `praxis_runner.py` — public CLI runner; parses arguments and hands the scenario to the core engine
- `scenarios/` — example scenario files (synthetic placeholder data only)
- `docs/architecture.md` — public architecture overview: scenario layer, runner layer, core layer, outputs
- `INSTALL_CORE.md` — how to install the private `praxis_core` wheel
- `LICENSE-NONCOMMERCIAL.txt`, `LICENSE-COMMERCIAL.txt` — licensing terms

## Licensing

This project uses a dual license model.

**Free research and academic license** — permitted for personal use, academic research, educational institutions, non-profit research, and internal testing and evaluation. Commercial use is not permitted under this license. See `LICENSE-NONCOMMERCIAL.txt`.

**Paid commercial / government / enterprise license** — required for for-profit company use, commercial product development, infrastructure operations, utilities and energy sector use, defense and government deployment, and consulting, resale, or SaaS use. Commercial licenses must be obtained directly from the author. See `LICENSE-COMMERCIAL.txt`.

Contact: darksciencedivision@gmail.com
