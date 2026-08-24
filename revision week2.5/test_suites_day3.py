import pytest
import json
from contract_review import updated_process_reading, load_sensor_data, updated_valid_reading
from exceptions import InvalidQuantumReadingError, InvalidSensorDataError

"""
# Goal: 
1. Use Fixtures to provide mock data and avoid repetition
2. Use Parametrization for single function to test repeatedly
3. tmp_path to avoid reading files from local directory
"""


# A crude way of using the fixture, the below is an anti-pattern
@pytest.fixture
def get_valid_schema_skeleton():
    return {"device_id": "abc", "backend": "simulator", "readings": []}


def test_updated_process_reading_all_incorrect_input(get_valid_schema_skeleton):
    output = {"device_id": "abc",
              "backend": "simulator",
              "total_readings": 4,
              "valid_readings": [],
              "invalid_readings": [("abc", "Invalid Value"), (None, "Invalid Value"), (1.2, "Out of boundary"),
                                   (-0.8, "Out of boundary")]}

    get_valid_schema_skeleton["readings"] = ["abc", None, 1.2, -0.8]

    result = updated_process_reading(get_valid_schema_skeleton)
    assert result == output


def test_updated_process_reading_all_correct_input(get_valid_schema_skeleton):
    output = {"device_id": "abc",
              "backend": "simulator",
              "total_readings": 3,
              "valid_readings": [(0, 0), (0.5, 0.25), (1, 1.0)],
              "invalid_readings": []}

    get_valid_schema_skeleton["readings"] = [0, 0.5, 1]

    result = updated_process_reading(get_valid_schema_skeleton)
    assert result == output


# fixture should be used only when the same input is used in multiple tests. When dynamic input is required following
# two methods can be used.

# 1. Define a factory fixture that returns a generation function
@pytest.fixture
def make_sensor_reading():
    def _create_reading(readings_list):
        return {
            "device_id": "abc",
            "backend": "simulator",
            "readings": readings_list
        }
    return _create_reading


def test_updated_process_reading_mixed_inputs(make_sensor_reading):
    output = {
        "device_id": "abc",
        "backend": "simulator",
        "total_readings": 5,
        "valid_readings": [(0, 0), (0.5, 0.25)],
        "invalid_readings": [("abc", "Invalid Value"), (None, "Invalid Value"), (1.2, "Out of boundary")]
    }

    mixed_sensor_reading = make_sensor_reading([0, "abc", None, 0.5, 1.2])
    assert output == updated_process_reading(mixed_sensor_reading)


def test_updated_process_reading_empty_input(make_sensor_reading):
    output = {
        "device_id": "abc",
        "backend": "simulator",
        "total_readings": 0,
        "valid_readings": [],
        "invalid_readings": []
    }
    empty_sensor_reading = make_sensor_reading([])
    assert output == updated_process_reading(empty_sensor_reading)


# 2. Using Parametrization for repeating the tests on different inputs and their expected outputs.
@pytest.mark.parametrize("sensor_reading, expected_output", [
    # All correct inputs
    ({"device_id": "abc", "backend": "simulator", "readings": [0, 0.5, 1]},
     {"device_id": "abc",
      "backend": "simulator",
      "total_readings": 3,
      "valid_readings": [(0, 0), (0.5, 0.25), (1, 1.0)],
      "invalid_readings": []}),

    # All incorrect inputs
    ({"device_id": "abc", "backend": "simulator", "readings": ["xyz", None, 1.5]},
     {"device_id": "abc",
      "backend": "simulator",
      "total_readings": 3,
      "valid_readings": [],
      "invalid_readings": [("xyz", "Invalid Value"), (None, "Invalid Value"), (1.5, "Out of boundary")]}),

    # Mixed inputs
    ({"device_id": "abc", "backend": "simulator", "readings": [0, "abc", None, 1.5, 1]},
     {"device_id": "abc",
      "backend": "simulator",
      "total_readings": 5,
      "valid_readings": [(0, 0), (1, 1.0)],
      "invalid_readings": [("abc", "Invalid Value"), (None, "Invalid Value"), (1.5, "Out of boundary")]})
])
def test_updated_process_reading_variety_inputs(sensor_reading, expected_output):
    result = updated_process_reading(sensor_reading)
    assert result == expected_output


# Parameterizing tests for updated_valid_reading
@pytest.mark.parametrize("reading, output", [
    (0, 0),
    (1, 1.0)
])
def test_updated_valid_reading_valid_inputs(reading, output):
    result = updated_valid_reading(reading)
    assert result == output


@pytest.mark.parametrize("reading, error_message", [
    (1.2, "Out of boundary"),
    (None, "Invalid Value"),
    ("pqr", "Invalid Value")
])
def test_updated_valid_reading_invalid_inputs(reading, error_message):
    with pytest.raises(InvalidQuantumReadingError, match=error_message):
        updated_valid_reading(reading)


# tmp_path to test file reading
def test_load_sensor_data_valid_path(tmp_path):
    temp_file = tmp_path / "valid_sensor.json"
    mock_data = {"device_id": "abc", "backend": "simulator", "readings": [1]}

    temp_file.write_text(json.dumps(mock_data), encoding="utf-8")

    result = load_sensor_data(temp_file)
    assert result == mock_data


def test_load_sensor_data_invalid_path(tmp_path):
    temp_file = tmp_path / "not a file.json"

    with pytest.raises(FileNotFoundError) as e:
        load_sensor_data(temp_file)
    assert "No file in the path: " in str(e.value)


def test_load_sensor_data_invalid_json(tmp_path):
    temp_file = tmp_path / "invalid_data.json"
    mock_data = "device_id"
    temp_file.write_text(mock_data, encoding="utf-8")

    with pytest.raises(InvalidSensorDataError) as e:
        load_sensor_data(temp_file)
    assert 'contains invalid JSON syntax' in str(e.value)
