import pytest
import json
from utilities import get_experiment_data
from exceptions import InvalidContentError


def test_get_experiment_data_valid_json(tmp_path):
    valid_file = tmp_path / "valid.json"
    mock_data = '''{
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

    valid_file.write_text(mock_data, 'utf-8')
    output = get_experiment_data(valid_file)

    assert json.loads(mock_data) == output


def test_get_experiment_data_invalid_json(tmp_path):
    temp_file = tmp_path / "wrong_path"
    mock_data = "Not JSON data"
    temp_file.write_text(mock_data, 'utf-8')

    with pytest.raises(InvalidContentError) as e:
        get_experiment_data(temp_file)
    assert 'Data in the file is not a valid JSON' in str(e.value)
