import pytest
import json
from utilities import get_experiment_data, validate_experiment, is_valid_result
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
