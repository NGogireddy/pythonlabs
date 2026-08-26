# Capstone --- Quantum Experiment Results Processor

------------------------------------------------------------------------

Reads results from multiple simulated quantum experiments in the below format

``` json
{
    "experiment_id": "EXP-001",
    "backend": "simulator",
    "shots": 1000,
    "results": [
        {"state": "00", "count": 482},
        {"state": "11", "count": 498},
        {"state": "01", "count": 12},
        {"state": "10", "count": 8}
    ]
}
```

------------------------------------------------------------------------

# Goal

Verify the data contract and the results with the following rules

1. experiment_id, backend, shots and results should be present.
2. results is a list or dictionaries each having state and count keys.
3. Following rules for each field 

``` text
experiment_id → non-empty string
backend       → non-empty string
shots         → positive integer
results       → list
state         → non-empty string
count         → non-negative integer
```
4. Process the results and produce a report.
5. Distinguish the errors between schema errors and the experiment results.
6. Do not stop for one invalid result. 
7. Establish clear data contracts between the modules
8. Create test cases for all the modules. 

------------------------------------------------------------------------

# High-level approach

1. run_app() -> to orchestrate the flow. 
2. get_experiment_data() -> read data from file and return JSON
3. validate_experiment() -> validate the data contract for experiment schema
4. process_experiment() -> process the results from the experiment
5. generate_report() -> print the report of the processed experiment

------------------------------------------------------------------------

``` text
pyproject.toml is to help import the functions in test folder without 
making src folder a package
```

------------------------------------------------------------------------
