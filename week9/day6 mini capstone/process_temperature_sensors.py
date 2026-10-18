import ast
import numpy as np

"""
This is a backend ingest system for thousands of solar-powered weather sensors placed across a city. Every 5 minutes, 
each sensor transmits a compressed packet (batch) of 1D telemetry readings (e.g., ambient temperature) to a central 
gateway. We process each batch and provide a summary at the end of an hour (once 12 batches are processed). 

The summary of all batches contains:
    1. Total number of readings
    2. Total valid and invalid readings
    3. Total number of batches received
    4. Sum of all valid readings
    5. Min of all readings batch
    6. Max of all readings
    7. Average of all valid readings
"""

"""
Before coding, define:

-   What is a valid batch?
    A valid batch is a 1D np array of int/floating numbers. Complex numbers are not allowed. No other dimensions are 
    valid, including empty array.
    
-   Are lists accepted, or only NumPy arrays?
    Only np arrays are accepted. Lists are not accepted. 
    
-   Are empty batches ignored or counted?
    Empty batches are ignored. 
    
-   Are NaN and infinity allowed?
    No NaN and inf are discarded from the readings including the average calculations. 
    
-   What happens if no valid values are accepted?
    The batch itself is ignored. 
    
-   Is the input mutated?
    No the input is not mutated. 
    
-   Is the whole input materialised?
    No the input is not materialised, only the summary of each batch is materialised. 
    
-   What does `count` count: batches, measurements, or both?
    The count has both the count of measurements and batches. 
"""


def parse_telemetry_string(input_string: str) -> np.ndarray:
    """
    Safely parses incoming network string configurations into standard NumPy arrays
    without relying on strict literal evaluation rules.
    """
    if not isinstance(input_string, str):
        return input_string

    cleaned = input_string.strip()

    # Strip the np.array([ ... ]) wrapper cleanly
    if cleaned.startswith("np.array(") and cleaned.endswith(")"):
        cleaned = cleaned[9:-1]
    if cleaned.startswith("[") and cleaned.endswith("]"):
        cleaned = cleaned[1:-1]

    # Handle the empty array edge case immediately
    if not cleaned.strip():
        return np.array([], dtype=float)

    # Split the inner string values by comma
    string_elements = cleaned.split(",")

    # Clean up whitespace and convert NumPy tokens to standard float strings
    float_elements = []
    for item in string_elements:
        item_cleaned = item.strip()
        if item_cleaned == "np.inf":
            item_cleaned = "inf"
        elif item_cleaned == "-np.inf":
            item_cleaned = "-inf"
        elif item_cleaned == "np.nan":
            item_cleaned = "nan"

        float_elements.append(float(item_cleaned))

    return np.array(float_elements, dtype=float)


def process_hourly_stream(batch_iterable, kelvin_offset: float = 273.15) -> dict:
    """
    Processes an hourly window of batches lazily using incremental tracking.
    """
    total_readings = 0
    total_valid_readings = 0
    total_invalid_readings = 0
    total_batches_received = 0
    sum_valid_readings = 0.0
    global_min = float('inf')
    global_max = float('-inf')

    for batch in batch_iterable:
        total_batches_received += 1

        # Contract Check 1: Structure validation (Must be a NumPy array)
        if not isinstance(batch, np.ndarray):
            # If it's a raw Python list primitive from a malformed batch
            batch_len = len(batch) if isinstance(batch, (list, tuple)) else 0
            total_readings += batch_len
            total_invalid_readings += batch_len
            continue

        batch_total_elements = batch.size
        total_readings += batch_total_elements

        if batch_total_elements == 0:
            continue

        # Contract Check 2: Dynamic Boolean Masking for finite data validation
        valid_mask = np.isfinite(batch)
        invalid_mask = ~valid_mask

        num_valid = np.count_nonzero(valid_mask)
        num_invalid = np.count_nonzero(invalid_mask)

        total_valid_readings += num_valid
        total_invalid_readings += num_invalid

        if num_valid == 0:
            continue

        # Requirement 3: Convert valid items to Kelvin
        valid_calibrated = batch[valid_mask] + kelvin_offset

        # Update rolling aggregates safely
        sum_valid_readings += np.sum(valid_calibrated)
        global_min = min(global_min, np.min(valid_calibrated))
        global_max = max(global_max, np.max(valid_calibrated))

    if total_valid_readings == 0:
        return {
            "total_readings": total_readings,
            "total_valid_readings": 0,
            "total_invalid_readings": total_invalid_readings,
            "total_batches_received": total_batches_received,
            "sum_valid_readings": 0.0,
            "min_reading": None,
            "max_reading": None,
            "average_valid_reading": None
        }

    return {
        "total_readings": total_readings,
        "total_valid_readings": total_valid_readings,
        "total_invalid_readings": total_invalid_readings,
        "total_batches_received": total_batches_received,
        "sum_valid_readings": float(sum_valid_readings),
        "min_reading": float(global_min),
        "max_reading": float(global_max),
        "average_valid_reading": float(sum_valid_readings / total_valid_readings)
    }
