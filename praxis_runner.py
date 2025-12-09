"""
PRAXIS Engine Public Runner

This script is part of the public interface for the PRAXIS risk and reliability engine.
The core numerical engine (praxis_core) is NOT included in this repository and is only
available under a commercial / government / enterprise license.

Free for research & academic use (see LICENSE-NONCOMMERCIAL.txt).
Commercial use requires a paid license (see LICENSE-COMMERCIAL.txt).
"""

import sys

def main():
    try:
        # This is the paid/private package you will distribute to customers.
        from praxis_core import run_engine  # pragma: no cover
    except ImportError:
        print("")
        print("PRAXIS Engine – Public Runner")
        print("--------------------------------")
        print("The public interface is installed, but the private core engine")
        print("(`praxis_core`) is not available in this environment.")
        print("")
        print("• Academic / research users: You can still inspect scenarios,")
        print("  data formats, and documentation in this repository.")
        print("")
        print("• Commercial / government / enterprise users:")
        print("  A paid license is required to obtain the PRAXIS core engine.")
        print("  Contact: darksciencedivision@gmail.com")
        print("")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: python praxis_runner.py <scenario_file>")
        sys.exit(1)

    scenario_path = sys.argv[1]
    run_engine(scenario_path)


if __name__ == "__main__":
    main()
