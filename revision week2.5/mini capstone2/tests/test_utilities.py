import pytest
import json
import time
from utilities import get_experiment_data, validate_experiment, is_valid_result, process_experiment_data, generate_report
from exceptions import InvalidContentError

VALID_JSON = '''{
    "experiment_id": "EXP-001",
    "backend": "simulator",
    "shots": 1000,
    "results": [
        {"state": "00", "count": 482},
        {"state": "11", "count": 498},
        {"state": "01", "count": 12},
        {"state": "10", "count": 8}
        ]
    }'''


def test_get_experiment_data_valid_json(tmp_path):
    valid_file = tmp_path / "valid.json"
    valid_file.write_text(VALID_JSON, 'utf-8')
    output = get_experiment_data(valid_file)

    assert json.loads(VALID_JSON) == output


def test_get_experiment_data_invalid_json(tmp_path):
    temp_file = tmp_path / "wrong_path"
    mock_data = "Not JSON data"
    temp_file.write_text(mock_data, 'utf-8')

    with pytest.raises(InvalidContentError) as e:
        get_experiment_data(temp_file)
    assert 'Not a valid JSON' in str(e.value)


def test_get_experiment_data_empty_json(tmp_path):
    temp_file = tmp_path / "empty_json.json"
    mock_data = '{}'
    temp_file.write_text(mock_data, encoding='utf-8')

    result = get_experiment_data(temp_file)
    assert result == json.loads(mock_data)


def test_get_experiment_data_empty_file(tmp_path):
    temp_file = tmp_path / "empty_file"
    mock_data = ""
    temp_file.write_text(mock_data, encoding='utf-8')

    with pytest.raises(InvalidContentError) as e:
        get_experiment_data(temp_file)
    assert 'Not a valid JSON' in str(e.value)


def test_validate_experiment_correct_data():
    result = validate_experiment(json.loads(VALID_JSON))
    assert result


@pytest.mark.parametrize("data, error_message", [
    ({"backend": "simulator", "shots": 10, "results": [{"01": 10}]},
     'experiment_id is missing or not a string or is empty'),
    ({"experiment_id": "", "backend": "simulator", "shots": 10, "results": [{"01": 10}]},
     'experiment_id is missing or not a string or is empty'),
    ({"experiment_id": 5, "backend": "simulator", "shots": 10, "results": [{"01": 10}]},
     'experiment_id is missing or not a string or is empty'),
    ({"experiment_id": "EXP-001", "shots": 10, "results": [{"01": 10}]},
     'backend is missing or not a string or is empty'),
    ({"experiment_id": "5", "backend": "", "shots": 10, "results": [{"01": 10}]},
     'backend is missing or not a string or is empty'),
    ({"experiment_id": "5", "backend": 5, "shots": 10, "results": [{"01": 10}]},
     'backend is missing or not a string or is empty'),
    ({"experiment_id": "EXP-001", "backend": "simulator", "shots": 0, "results": [{"01": 10}]},
     'shots is missing or not a positive integer'),
    ({"experiment_id": "EXP-001", "backend": "simulator", "shots": -10, "results": [{"01": 10}]},
     'shots is missing or not a positive integer'),
    ({"experiment_id": "EXP-001", "backend": "simulator", "results": [{"01": 10}]},
     'shots is missing or not a positive integer'),
    ({"experiment_id": "EXP-001", "backend": "simulator", "shots": 10},
     'results is missing or not a list'),
    ({"experiment_id": "EXP-001", "backend": "simulator", "shots": 10, "results": []},
     'results is missing or not a list or is empty'),
])
def test_validate_experiment_incorrect_scenarios(data, error_message):
    with pytest.raises(InvalidContentError, match=error_message):
        validate_experiment(data)


@pytest.mark.parametrize("result, error_message", [
    ({"state": "00", "count": -10}, 'count is missing or is not a positive Integer'),
    ({"state": "00", "count": 0}, 'count is missing or is not a positive Integer'),
    ({"state": "00", "counts": 10}, 'count is missing or is not a positive Integer'),
    ({"state": ""}, 'state is missing or is not a non-empty string'),
    ({"": 10}, 'state is missing or is not a non-empty string'),
    ({"state": 5}, 'state is missing or is not a non-empty string'),
])
def test_is_valid_result_invalid_scenarios(result, error_message):
    with pytest.raises(InvalidContentError, match=error_message):
        is_valid_result(result)


def test_is_valid_result_valid_scenario():
    exp_result = {"state": "01", "count": 10}
    assert is_valid_result(exp_result)


@pytest.mark.parametrize("experiment, expected_summary", [
    ({"experiment_id": "abc", "backend": "4 valid states", "shots": 100,
      "results": [{"state": "00", "count": 42}, {"state": "11", "count": 39}, {"state": "01", "count": 9},
                  {"state": "10", "count": 10}, {"states": '01', 'count':12}, {"state": "abc", "count": -10},
                  {"state": "def", "counts": 10}, {"state": 10, "count": "01"}]},
     {"experiment_id": "abc", "total_shots": 100, "valid_shots": 100, "unique_states": ['00', '11', '01', '10'],
        "probabilities": [{'00': 0.42}, {'11': 0.39}, {'01': 0.09}, {'10': 0.1}],
        "most_probable_state": "00",
        "invalid_results": [({'states': '01', 'count': 12}, 'state is missing or is not a non-empty string'),
                         ({'state': 'abc', 'count': -10}, 'count is missing or is not a positive Integer'),
                         ({'state': 'def', 'counts': 10}, 'count is missing or is not a positive Integer'),
                         ({'state': 10, 'count': '01'}, 'state is missing or is not a non-empty string')]
     }),
    ({"experiment_id": "def", "backend": "1 valid state", "shots": 10, "results": [{"state": "00", "count": 10}]}, {"experiment_id": "def", "total_shots": 10, "valid_shots": 10, "unique_states": ['00'], "probabilities": [{'00': 1.0}], "most_probable_state": "00", "invalid_results": []}),
    ({"experiment_id": "ghi", "backend": "2 valid state", "shots": 100,
      "results": [{"state": "00", "count": 48}, {"state": "11", "count": 49}]},
     {"experiment_id": "ghi", "total_shots": 100, "valid_shots": 97, "unique_states": ['00', '11'],
      "probabilities": [{'00': 0.48}, {'11': 0.49}], "most_probable_state": "11", "invalid_results": []}),
])
def test_process_experiment_data_valid_json(experiment, expected_summary):
    result = process_experiment_data(experiment)
    assert result == expected_summary


def test_process_experiment_data_7_qubits():
    # 1. Setup constants
    num_qubits = 7
    total_shots = 100000
    num_states = 2 ** num_qubits  # 128

    # Evenly distribute shots across 127 states (100000 // 128 = 781)
    base_count = total_shots // num_states
    # Hand the remaining remainder shots to the very first state so total matches perfectly
    remainder = total_shots % num_states

    # 2. Programmatically generate the 128 states & counts
    generated_results = []
    expected_probabilities = []
    expected_unique_states = []

    for i in range(num_states):
        # Generate 7-bit binary string (e.g., 0 -> "0000000", 1 -> "0000001", etc.)
        state_str = f"{i:0{num_qubits}b}"

        # Give the first state ("0000000") the remainder so total shots sum to 100,000
        count = base_count + remainder if i == 0 else base_count

        generated_results.append({"state": state_str, "count": count})
        expected_unique_states.append(state_str)
        expected_probabilities.append({state_str: count / total_shots})

    # 3. Assemble the massive input payload
    large_experiment = {
        "experiment_id": "EXP-7Q",
        "backend": "128-state-simulator",
        "shots": total_shots,
        "results": generated_results
    }

    # 4. Construct what the perfect matching output summary should be
    expected_summary = {
        "experiment_id": "EXP-7Q",
        "total_shots": total_shots,
        "valid_shots": total_shots,  # Every generated row is valid
        "unique_states": expected_unique_states,
        "probabilities": expected_probabilities,
        "most_probable_state": "0000000",  # Holds the base count + remainder
        "invalid_results": []
    }

    # 5. Execute and assert
    start_time = time.perf_counter()
    actual_summary = process_experiment_data(large_experiment)
    end_time = time.perf_counter()
    print(f'Run time for 7 bit experiment result: {end_time - start_time}')
    assert actual_summary == expected_summary


def test_process_experiment_data_14_qubits():
    # 1. Setup constants
    num_qubits = 14
    total_shots = 10_000_000
    num_states = 2 ** num_qubits

    # Evenly distribute shots across all states
    base_count = total_shots // num_states
    # Hand the remaining remainder shots to the very first state so total matches perfectly
    remainder = total_shots % num_states

    # 2. Programmatically generate the states & counts
    generated_results = []
    expected_probabilities = []
    expected_unique_states = []

    for i in range(num_states):
        # Generate 14-bit binary string (e.g., 0 -> "00000000000000", 1 -> "00000000000001", etc.)
        state_str = f"{i:0{num_qubits}b}"

        # Give the first state ("00000000000000") the remainder so total shots sum to 10_000_000
        count = base_count + remainder if i == 0 else base_count

        generated_results.append({"state": state_str, "count": count})
        expected_unique_states.append(state_str)
        expected_probabilities.append({state_str: count / total_shots})

    # 3. Assemble the massive input payload
    large_experiment = {
        "experiment_id": "EXP-14Q",
        "backend": "perf-simulator",
        "shots": total_shots,
        "results": generated_results
    }

    # 4. Construct what the perfect matching output summary should be
    expected_summary = {
        "experiment_id": "EXP-14Q",
        "total_shots": total_shots,
        "valid_shots": total_shots,  # Every generated row is valid
        "unique_states": expected_unique_states,
        "probabilities": expected_probabilities,
        "most_probable_state": "00000000000000",  # Holds the base count + remainder
        "invalid_results": []
    }

    # 5. Execute and assert
    start_time = time.perf_counter()
    actual_summary = process_experiment_data(large_experiment)
    end_time = time.perf_counter()
    print(f'Run time for 14 bit experiment result: {end_time - start_time}')
    assert actual_summary == expected_summary


def test_generate_report_none_input(capsys):
    generate_report(None)
    captured = capsys.readouterr()
    console_output = captured.out

    assert console_output == ""


def test_generate_report_valid_input(capsys):
    summary = {"experiment_id": "abc", "total_shots": 100, "valid_shots": 100, "unique_states": ['00', '11', '01', '10'],
        "probabilities": [{'00': 0.42}, {'11': 0.39}, {'01': 0.09}, {'10': 0.1}],
        "most_probable_state": "00",
        "invalid_results": [({'states': '01', 'count': 12}, 'state is missing or is not a non-empty string'),
                         ({'state': 'abc', 'count': -10}, 'count is missing or is not a positive Integer'),
                         ({'state': 'def', 'counts': 10}, 'count is missing or is not a positive Integer'),
                         ({'state': 10, 'count': '01'}, 'state is missing or is not a non-empty string')]
    }

    generate_report(summary)
    captured = capsys.readouterr()
    console_output = captured.out

    assert 'Experiment ID' in console_output
    assert 'Total shots' in console_output
    assert 'Valid shots' in console_output
    assert 'Unique states' in console_output
    assert 'Most likely state' in console_output
    assert 'Probabilities' in console_output
    assert 'Invalid results' in console_output
    assert 'count is missing or is not a positive Integer' in console_output
    assert 'state is missing or is not a non-empty string' in console_output
