import numpy as np
from pathlib import Path
from collections import defaultdict


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


# Generator to read the lines in each file and return it
def read_experiment_results(file_path=None):
    if file_path is None:
        file_path = Path(__file__).resolve().parent / "experiment_results"

    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip(',\n')


# Convert experiment to np array
def convert_exp_numpy(raw_results):
    for result in raw_results:
        safe_environment = {"np": np, "numpy": np}
        try:
            # Evaluate the string within the safe sandbox
            output = eval(result, safe_environment, {})

            # Validate that the evaluated output is actually a NumPy array
            if isinstance(output, np.ndarray) and output.ndim == 1 and output.dtype.kind in 'iuf':
                yield output
        except (SyntaxError, NameError, TypeError, ValueError):
            yield np.empty([0])


# function to validate if the record is a valid experiment result record
def is_valid_experiment(result):
    safe_environment = {"np": np, "numpy": np}
    try:
        # Evaluate the string within the safe sandbox
        output = eval(result, safe_environment, {})

        # Validate that the evaluated output is actually a NumPy array
        if isinstance(output, np.ndarray) and output.ndim == 1 and output.dtype.kind in 'iuf':
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
    summary["mean"] = float(cleansed_results.mean())
    summary["min"] = float(cleansed_results.min())
    summary["max"] = float(cleansed_results.max())
    print(summary)


def process_results():
    """
    Appends the np array results which are valid and calculates total, min and max lazily
    :return: summary
    """
    summary = defaultdict(int)
    current_min = None
    current_max = None
    raw_stream = read_experiment_results()
    converted_array_stream = convert_exp_numpy(raw_stream)
    for result in converted_array_stream:
        valid_results = result[result > 0]
        if valid_results.size > 0:
            summary["experiment_count"] += 1
            summary["valid_results"] += valid_results.size
            summary["result_total"] += float(valid_results.sum())

            batch_min = float(valid_results.min())
            batch_max = float(valid_results.max())

            if current_min is None:
                current_min = batch_min
                current_max = batch_max
            else:
                current_min = min(current_min, batch_min)
                current_max = max(current_max, batch_max)

    summary["min"] = current_min
    summary["max"] = current_max
    if summary["valid_results"] > 0:
        summary["mean"] = summary["result_total"] / summary["valid_results"]
    else:
        summary["mean"] = 0
    print(summary)


# main function.
if __name__ == "__main__":
    process_results()
    process_experiment()

"""
Reflection: 
process_experiment is the flow done on Day6 and process_results is the flow done on Day7. 
Day6 processing is partially lazy and accumulating all the valid results before calculating the min, max and mean. It is
not memory efficient when there are millions of valid experiment results.
Day7 processing is fully lazy and processes each result one after the other. This is memory efficient but the if
conditions inside the loop would take additional time. We are not using the numpy features efficiently here. I was not 
able to complete the test cases for all the methods as it was taking too much time. 

Self Evaluation: 
  Area                                Score
  --------------------------------- -------
  NumPy array fundamentals               4/5
  Shape and dimensional reasoning        4/5
  Indexing and slicing                   5/5
  Views and copies                       5/5
  Vectorisation                          5/5
  Boolean masks                          5/5
  Broadcasting                           4/5
  Numerical aggregation                  5/5
  Data contracts                         4/5
  Test quality                           4/5
  Floating-point testing                 4/5
  Performance awareness                  4/5
  Engineering judgement                  4/5
  Refactoring                            4/5

"""