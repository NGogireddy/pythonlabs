
# Week 14 — From NumPy Quantum Circuits to Qiskit

## Overview

This project marks the transition from implementing quantum computing concepts using Python and NumPy to building and executing quantum circuits using Qiskit.

The objective is to understand how quantum states, quantum gates, measurements, and multi-qubit operations are represented using a quantum circuit SDK.

Qiskit will be used to construct and execute circuits, while the concepts and mathematical foundations developed in previous weeks will serve as the reference for understanding the results.

## Learning Objectives

By the end of Week 14, I aim to:

- Understand the structure of a Qiskit quantum circuit.
- Create circuits using Qiskit's circuit abstractions.
- Apply quantum gates such as X, Z, and Hadamard.
- Measure qubits and interpret measurement counts.
- Prepare and explore all four Bell states.
- Understand correlations between two entangled qubits.
- Implement and verify a Bell-state decoder.
- Compare Qiskit simulator results with previous NumPy implementations.

## Technology Stack

| Component | Version | Purpose |
|---|---|---|
| Python | 3.14.0 | Programming language |
| Qiskit | 2.6.2 | Quantum circuit SDK |
| Qiskit Aer | 0.18.2 | Local quantum circuit simulator |
| NumPy | Installed as a dependency | Numerical reference calculations |

## Project Structure

```text
week14_qiskit/
│
├── .venv/                  # Local virtual environment (not committed)
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
│
├── day1/                   # Environment setup and SDK orientation
├── day2/                   # First quantum circuit
├── day3/                   # Measurements and shot counts
├── day4/                   # Preparation of four Bell states
├── day5/                   # Bell-state measurements in X basis
├── day6/                   # Bell-state decoder
└── day7/                   # Bell-state explorer capstone
```

*Daily folders will be added as the exercises are completed.*

## Environment Setup

This project uses an isolated Python virtual environment.

### 1. Create the virtual environment

```bash
python3 -m venv .venv
```

### 2. Activate the environment (macOS/Linux)

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Verify installation

```bash
python -c "import qiskit, qiskit_aer; print('Qiskit:', qiskit.__version__); print('Qiskit Aer:', qiskit_aer.__version__)"
```

## Quantum Computing Background

This project builds on the concepts explored in previous weeks:

- Complex probability amplitudes and normalization.
- Single-qubit gates: Pauli-X, Pauli-Z, and Hadamard.
- Two-qubit states and tensor products.
- Controlled-NOT (CNOT) operations.
- Bell-state preparation and entanglement.
- Measurement probabilities and quantum correlations.
- Bell-state decoding.

The focus is on understanding how these concepts translate from explicit NumPy matrix operations into Qiskit circuit operations.

## Simulator

Qiskit Aer provides a local simulator for executing quantum circuits without requiring access to physical quantum hardware.

Unless explicitly stated otherwise, experiments in this project use ideal simulation. Measurement results may vary between runs because of random sampling.

## Learning Approach

- Understand the underlying quantum concept before implementing it.
- Predict expected outcomes before executing circuits.
- Validate simulator results against mathematical expectations.
- Write meaningful tests and checks.
- Prefer clear, maintainable Python code over unnecessary complexity.

## Repository

[Python Labs — GitHub](https://github.com/NGogireddy/pythonlabs)
