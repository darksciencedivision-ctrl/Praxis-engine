# PRAXIS Engine – High-Level Architecture

This document describes the *public* architecture of the PRAXIS risk and reliability engine.

At a high level:

1. **Scenario Layer**  
   - YAML / JSON input describing systems, domains, stressors, and dependencies.  
   - Example: `scenarios/example_blackswan_saturday.yaml`.

2. **Interface / Runner Layer (Public)**  
   - `praxis_runner.py` parses CLI arguments and passes the scenario file path to the core engine.  
   - This repository exposes the runner and data formats for academic and research use.

3. **Core Engine Layer (Private / Licensed)**  
   - Implemented in the `praxis_core` package.  
   - Contains numerical risk, Bayesian update, PRA propagation, and lifecycle reliability logic.  
   - Not included in this public repository. Distributed only under a paid commercial / government / enterprise license.

4. **Outputs**  
   - Structured text or JSON outputs summarizing:  
     - Domain risk scores  
     - Failure modes  
     - Cascading effects  
     - Lifecycle reliability metrics

For academic users, this repository is intended to make the interface and scenario structure transparent
while keeping the proprietary numerical engine closed and licensable.
