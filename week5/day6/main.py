"""
## Problem

Imagine simulated quantum measurement data. Each experiment produces a 1D NumPy array of numerical measurement
values. You receive multiple experiments and need combined statistics.

Example:

[
    np.array([0.1, 0.2, 0.3]),
    np.array([0.4, 0.5, 0.6]),
    np.array([0.7, 0.8, 0.9]),
]

Calculate:

{
    "experiment_count": ...,
    "measurement_count": ...,
    "mean": ...,
    "minimum": ...,
    "maximum": ...
}
"""
import path

"""
## Input Contract

The input is an iterable of 1D NumPy arrays.

- Are zero experiments allowed?  These are allowed and counted under experiment_count but will not impact output
- Are empty measurement arrays allowed? These are allowed and counted under experiment_count but will not impact output
- Must every experiment have the same number of measurements? Not really, it should just be a 1D np.ndarray
- Are NaN values allowed?  NaN values may appear in the results but will be ignored, they do not count to measurements 
- Are infinite values allowed?  No, infinite values are not allowed and will not be considered as a measurement
- Are integer arrays allowed? Normal lists/tuples are not allowed, it should be a np.ndarray they can be int/float
- Are floating-point arrays allowed?  Same as above. It should be np.ndarray of 1D and dtype should be int/float
- What happens for non-array input?  Experiment will be discarded. 
- What happens for a 2D array where a 1D array is expected? Experiment will be discarded
- What happens if experiment lengths differ? Experiment will be accepted as long as it is 1D int/float np.ndarray

Note: Each experiment should be in coming in one line. experiment results should be positive values (>0) 
"""

"""
## Output Contract

The output contains: 
- number of experiments 
- total number of measurements 
- combined mean 
- combined minimum 
- combined maximum

Any experiment results that are not 1D np arrays of type int/float will be discarded. Invalid experiments are not logged
"""

import numpy as np
from pathlib import Path
from collections import defaultdict

arr = np.array([1, -2, 0])
out = np.array([4, np.nan])
empty = np.empty((0))
print(out.dtype)
out = np.concatenate((out, arr))
print(out)

out = np.concatenate((out, empty))
print(out)
print(out[out > 0])


# Generator to read the lines in each file and return it
def read_experiment_results():
    file_dir = Path(__file__).resolve().parent / "experiment_results"
    with open(file_dir, 'r') as file:
        for line in file:
            yield line.strip(',\n')


# function to validate if the record is a valid experiment result record
def is_valid_experiment(result):
    safe_environment = {"np": np, "numpy": np}
    try:
        # Evaluate the string within the safe sandbox
        output = eval(result, safe_environment, {})

        # Validate that the evaluated output is actually a NumPy array
        if isinstance(output, np.ndarray) and output.ndim==1 and output.dtype.kind in 'iuf':
            return True
    except (SyntaxError, NameError, TypeError, ValueError):
        pass
    return False


# function to convert result into np array
def convert_to_nparray(result):
    safe_environment = {"np": np, "numpy": np}
    return eval(result, safe_environment, {})


# Orchestrating function
def process_experiment():
    summary = defaultdict(int)
    results = np.empty([0])
    for result in read_experiment_results():
        if is_valid_experiment(result):
            summary["experiment_count"] += 1
            results = np.concatenate((results, convert_to_nparray(result)))
    cleansed_results = results[results > 0]
    summary["valid_results"] = cleansed_results.size
    summary["mean"] = cleansed_results.mean()
    summary["min"] = cleansed_results.min()
    summary["max"] = cleansed_results.max()


# main function.
if __name__ == "__main__":
    process_experiment()
