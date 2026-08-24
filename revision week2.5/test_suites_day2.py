import pytest
from pathlib import Path
from contract_review import load_sensor_data, generate_report, updated_process_reading, valid_schema, \
    updated_valid_reading
from exceptions import InvalidSensorDataError, InvalidQuantumReadingError


data_dir = Path.cwd() / "revision week2.5" / "data"


def test_updated_valid_reading_valid_input():
    assert isinstance(updated_valid_reading(0.5), float)


def test_updated_valid_reading_out_of_bound_exception():
    with pytest.raises(InvalidQuantumReadingError) as e:
        updated_valid_reading(-0.5)
    assert str(e.value) == "Out of boundary"


def test_updated_valid_reading_string_input():
    with pytest.raises(InvalidQuantumReadingError) as e:
        updated_valid_reading("abc")
    assert str(e.value) == "Invalid Value"


def test_updated_valid_reading_nonetype_input():
    with pytest.raises(InvalidQuantumReadingError) as e:
        updated_valid_reading(None)
    assert str(e.value) == "Invalid Value"


def test_updated_valid_reading_list_input():
    with pytest.raises(InvalidQuantumReadingError) as e:
        updated_valid_reading([1])
    assert str(e.value) == "Invalid Value"


def test_load_sensor_data_no_file():
    with pytest.raises(FileNotFoundError) as e:
        load_sensor_data("Invalidpath")
    assert str(e.value) == "No file in the path: Invalidpath"


def test_load_sensor_data_invalid_json():
    invalid_file = data_dir / "invalid_json.json"
    with pytest.raises(InvalidSensorDataError) as e:
        load_sensor_data(invalid_file)

    error_msg = str(e.value)
    assert f"File at {invalid_file} contains invalid JSON syntax" in error_msg


def test_load_sensor_data_valid_input():
    expected_json = {'device_id': 'Q-SENSOR-001',
                     'backend': 'simulator',
                     'readings': [0.5, {'key': 'value'}, None, 0.9, 1.2, None, -0.8, 0.25]
                     }
    input_file = data_dir / "sensor_data.json"
    result = load_sensor_data(input_file)
    assert expected_json == result


def test_load_sensor_data_empty_file():
    empty_file = data_dir / "empty_file.json"
    with pytest.raises(InvalidSensorDataError) as e:
        load_sensor_data(empty_file)

    error_msg = str(e.value)
    assert "contains invalid JSON syntax" in error_msg


def test_valid_schema_invalid_schema():
    invalid_schema = {"deviceid": "abc", "readings": []}
    with pytest.raises(InvalidSensorDataError) as e:
        valid_schema(invalid_schema)

    error_msg = str(e.value)
    assert f' is not a valid schema for sensor data' in error_msg


def test_valid_schema_empty_schema():
    empty_schema = {}
    with pytest.raises(InvalidSensorDataError) as e:
        valid_schema(empty_schema)

    error_msg = str(e.value)
    assert f' is not a valid schema for sensor data' in error_msg


def test_valid_schema_incorrect_readings_type():
    incorrect_readings_schema = {
        "device_id": "abc",
        "backend": "simulator",
        "readings": 1
    }
    with pytest.raises(InvalidSensorDataError) as e:
        valid_schema(incorrect_readings_schema)

    error_message = str(e.value)
    assert f'is not a valid schema for sensor data' in error_message


def test_valid_schema_positive_test():
    correct_schema = {
        "device_id": "abc",
        "backend": "simulator",
        "readings": [1, 0.5, None, "abc"]
    }
    assert valid_schema(correct_schema) is True


def test_updated_process_reading_mixed_input():
    output = {"device_id": "abc",
              "backend": "simulator",
              "total_readings": 8,
              "valid_readings": [(0.5, 0.25), (0.9, 0.81), (0.25, 0.0625)],
              "invalid_readings": [("abc", "Invalid Value"), (None, "Invalid Value"), (1.2, "Out of boundary"),
                                   (None, "Invalid Value"), (-0.8, "Out of boundary")]}

    sensor_reading = {"device_id": "abc", "backend": "simulator",
                      "readings": [0.5, "abc", None, 0.9, 1.2, None, -0.8, 0.25]
                      }

    result = updated_process_reading(sensor_reading)
    assert result == output


def test_updated_process_reading_all_correct_input():
    output = {"device_id": "abc",
              "backend": "simulator",
              "total_readings": 3,
              "valid_readings": [(0.5, 0.25), (0.9, 0.81), (0.25, 0.0625)],
              "invalid_readings": []
              }

    sensor_reading = {"device_id": "abc", "backend": "simulator",
                      "readings": [0.5, 0.9, 0.25]
                      }

    result = updated_process_reading(sensor_reading)
    assert result == output


def test_updated_process_reading_all_incorrect_input():
    output = {"device_id": "abc",
              "backend": "simulator",
              "total_readings": 4,
              "valid_readings": [],
              "invalid_readings": [("abc", "Invalid Value"), (None, "Invalid Value"), (1.2, "Out of boundary"),
                                   (-0.8, "Out of boundary")]}

    sensor_reading = {"device_id": "abc", "backend": "simulator",
                      "readings": ["abc", None, 1.2, -0.8]
                      }

    result = updated_process_reading(sensor_reading)
    assert result == output


def test_updated_process_reading_empty_readings():
    output = {"device_id": "abc",
              "backend": "simulator",
              "total_readings": 0,
              "valid_readings": [],
              "invalid_readings": []}

    sensor_reading = {"device_id": "abc", "backend": "simulator",
                      "readings": []
                      }

    result = updated_process_reading(sensor_reading)
    assert result == output


def test_generate_report_empty_input(capsys):
    generate_report(None)
    captured = capsys.readouterr()

    assert captured.out == ""


def test_generate_report_simple_report(capsys):
    report = {"device_id": "abc",
              "backend": "simulator",
              "total_readings": 8,
              "valid_readings": [(0.5, 0.25), (0.9, 0.81), (0.25, 0.0625)],
              "invalid_readings": [("abc", "Invalid Value"), (None, "Invalid Value"), (1.2, "Out of boundary"),
                                   (None, "Invalid Value"), (-0.8, "Out of boundary")]}

    generate_report(report)

    captured = capsys.readouterr()
    console_output = captured.out

    assert "Device ID        : abc" in console_output
    assert "Backend          : simulator" in console_output
    assert "Total readings   : 8" in console_output
    assert "0.5    -> 0.25" in console_output
    assert "abc    -> Invalid Value" in console_output
    assert "Processing Status: COMPLETED" in console_output
