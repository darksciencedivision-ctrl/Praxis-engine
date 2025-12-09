# Installing the PRAXIS Core Engine (`praxis_core`)

The public `Praxis-engine` repository contains:

- The CLI runner: `praxis_runner.py`
- Scenario examples: `scenarios/`
- Documentation: `docs/`
- Licensing terms

The **numerical core engine** is packaged separately as a private
Python package called **`praxis_core`**. It is not published in this
repository and is only available under a commercial / government /
enterprise license (or under specific research agreements).

---

## 1. Requirements

- Python 3.9 or newer
- Ability to install Python packages with `py -m pip`
- A valid PRAXIS core engine wheel file, for example:

```text
praxis_core-0.1.0-py3-none-any.whl
