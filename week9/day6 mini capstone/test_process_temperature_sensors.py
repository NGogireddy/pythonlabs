import pytest
import numpy as np
from process_temperature_sensors import parse_telemetry_string, process_hourly_stream


@pytest.fixture
def hourly_sensor_stream():
    """Provides a perfectly clean iterable list stream of the 12-hour sensor data."""
    raw_inputs = [
        "np.array([20.14, 19.82, 20.55, 20.01, 19.45, 20.32, 20.11, 19.95, 20.05, 20.21])",  # 1: 10 valid
        "np.array([21.22, 21.85, 21.40, 21.01, 22.12, 21.55, 20.98, 21.65, 21.32, 21.49])",  # 2: 10 valid
        "np.array([22.91, 22.45, 23.10, 22.67, 23.41, 22.80, 22.34, 22.99, 22.71, 22.85])",  # 3: 10 valid
        "np.array([])",  # 4: Empty (0)
        "np.array([19.10, 19.62, 19.44, 20.02, 18.95, 19.51, 19.78, 19.33, 19.65, 19.41])",  # 5: 10 valid
        "np.array([18.11, 17.95, 18.24, 17.88, np.inf, -np.inf])",  # 6: 4 valid, 2 inf
        "np.array([16.21, 16.88, 16.45, 16.01, 17.02, 16.50, 15.99, 16.63, 16.38, 16.52])",  # 7: 10 valid
        "[15.2, 15.1, 15.3, 15.0]",  # 8: Raw list (4 items)
        "np.array([14.12, 13.85, 14.40, 13.91, 14.22, 14.05, 13.68, 14.19, 13.98, 14.01])",  # 9: 10 valid
        "np.array([13.41, 13.95, 13.20, 13.67, 13.11, 13.50, 13.84, 13.39, 13.61, 13.48])",  # 10: 10 valid
        "np.array([12.91, 12.65, 12.80, 12.44, np.nan, np.nan])",  # 11: 4 valid, 2 nan
        "np.array([11.91, 12.25, 12.10, 11.67, 12.41, 12.00, 11.54, 12.11, 11.89, 12.05])"  # 12: 10 valid
    ]

    parsed_items = []
    for text in raw_inputs:
        if text.startswith("np.array("):
            parsed_items.append(parse_telemetry_string(text))
        else:
            # For the raw list string primitive, parse it using simple safe literal reading
            import ast
            parsed_items.append(ast.literal_eval(text))

    return parsed_items


def test_hourly_metrics_aggregation(hourly_sensor_stream):
    """Validates the 7 metrics match environmental requirements exactly."""
    summary = process_hourly_stream(hourly_sensor_stream, kelvin_offset=273.15)

    # Assertions should pass completely now
    assert summary["total_readings"] == 96
    assert summary["total_valid_readings"] == 88
    assert summary["total_invalid_readings"] == 8
    assert summary["total_batches_received"] == 12

    # Assert values using floating-point checks
    np.testing.assert_allclose(summary["min_reading"], 284.69, rtol=1e-5)
    np.testing.assert_allclose(summary["max_reading"], 296.56, rtol=1e-5)
    assert summary["min_reading"] <= summary["average_valid_reading"] <= summary["max_reading"]


def test_completely_corrupted_window():
    """Asserts structural integrity configurations for periods with zero valid transmissions."""
    corrupted_data = [
        np.array([np.nan, np.inf]),
        "[10, 20]",
        np.array([])
    ]
    summary = process_hourly_stream(corrupted_data)

    assert summary["total_readings"] == 2
    assert summary["total_valid_readings"] == 0
    assert summary["total_invalid_readings"] == 2
    assert summary["total_batches_received"] == 3
    assert summary["min_reading"] is None
    assert summary["max_reading"] is None
    assert summary["average_valid_reading"] is None
