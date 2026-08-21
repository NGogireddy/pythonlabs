# Mini Capstone: Quantum Sensor Data Pipeline

A production-grade Python application designed to ingest, validate, cleanse, and process quantum telemetry records from local filesystem sources. 

The core objective of this project is to apply robust structural design patterns, object-oriented file routing with `pathlib`, granular custom error mapping, and protective data stream decoupling.

---

## 🏗️ Project Architecture & Modules

The codebase enforces strict separation of concerns across localized Python modules:

```text
mini_capstone/
│
├── data/
│   └── sensor_data.json         # Single JSON test asset payload
│
├── exceptions.py                # Definition of localized domain exception classes
├── validator.py                 # Algorithmic JSON schema and boundary checks
├── processor.py                 # Core file parsing loops and metric state machines
├── main.py                      # Application entry orchestrator and CLI reporting
└── README.md                    # System documentation
```

### Module Blueprint Breakdown:
* **`exceptions.py`**: Declares decoupled exceptions (`InvalidSensorDataError`, `InvalidQuantumReadingError`) embedded with debugging attributes like `device_id` and `reading`.
* **`validator.py`**: Acts as a gateway. Validates structural presence of keys and verifies that numerical sensor inputs fall cleanly within bounds `[0, 1]`.
* **`processor.py`**: Executes file reading operations safely inside context managers (`with open`). Maps individual data records via the validation engine and aggregates success metrics.
* **`main.py`**: Safely locates physical assets relative to code locations using absolute `pathlib` resolutions, runs the parsing engine, and prints an aligned production console report.

---

## 🚀 Getting Started & Execution

### 1. Prerequisites
Ensure you have Python 3.10 or newer installed on your machine. This project relies entirely on native standard libraries—no external `pip` installations are required.

### 2. Setup Local Data
Ensure your data assets are inside the `data/` folder relative to the script execution path. Your JSON files should resemble this schema footprint:
```json
{
    "device_id": "Q-SENSOR-001",
    "backend": "simulator",
    "readings": [0.25, 0.81, null, -0.20, 1.44]
}
```

### 3. Run the Pipeline
To execute the pipeline safely without absolute import path collisions, navigate your system terminal into the root directory of the project and execute `main.py`:

```bash
cd path/to/mini_capstone
python main.py
```

---

## 🔒 Production Defenses & Error Handling

Rather than crashing catastrophically when encountering corrupted payloads, the application implements active boundary protection:
1. **File Crash Immunity:** Completely empty `.json` payloads are intercepted safely using size checks and `json.JSONDecodeError` traps.
2. **Line Isolation:** For streaming `.jsonl` sets, a corruption in a single message string raises an isolated `InvalidSensorDataError`. This line is logged gracefully to stdout as a warning while the underlying process shifts to the next record without halting.
3. **Data Type & Bound Safety:** String literals, null elements (`None`), and negative values out of scientific ranges are caught line-by-line via `InvalidQuantumReadingError`, allowing clean floats to process seamlessly.

---

## 📊 Sample Consolidated Terminal Output

When executed successfully, the application prints a formatted, vertically-aligned processing audit ledger:

```text
=============================================
       QUANTUM SENSOR PROCESSING REPORT       
=============================================

Device ID        : Q-SENSOR-001
Backend          : simulator 

Total readings   : 6
Valid readings   : 4
Invalid readings : 2

Valid results
-------------
0.25     -> 0.0625
0.81     -> 0.6561
0.36     -> 0.1296

Invalid results
-------------
None     -> Invalid Value
-0.2     -> Out of boundary

Processing Status: COMPLETED
=============================================
```
