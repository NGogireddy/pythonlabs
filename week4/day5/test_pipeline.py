import pytest
import inspect
import json
from datetime import datetime
from pipeline import is_valid_float, log_error_records, get_experiment_data, validate_results, transform_result, \
    process_stream


@pytest.mark.parametrize("value, output", [
    ("4.2", True),
    ("0", True),
    ("abc", False),
    ("{1:2}}", False),
    ("", False),
    ("None", False),
])
def test_is_valid_float(value, output):
    result = is_valid_float(value)
    assert result == output


def test_log_error_records(tmp_path):
    error_log_file = tmp_path / "errors.log"

    # 2. Run the function under test
    test_record = '{"experiment_id": "EXP-401", "status": "ERROR"}'
    log_error_records(test_record, error_log_file)

    # 3. Locate the generated file inside the tmp_path
    expected_file = tmp_path / "errors.log"

    # 4. Assertions
    assert expected_file.exists()

    # Read the file content to verify correctness
    file_content = expected_file.read_text()
    assert file_content == f"{test_record}\n"


@pytest.fixture
def sample_results():
    rec1 = '{"timestamp": "2026-09-09 10:00:00", "experiment_id": "EXP-401", "sensor_reading": "45.2", "status": "OK"},\n'
    rec2 = '{"timestamp": "2026-09-09 10:01:00", "exp_id": "EXP-401", "sensor_reading": "ERR", "status": "FAIL"},\n'
    rec3 = '{"timestamp": "2026-09-09 10:02:00", "exp_id": "EXP-401", "sensor_reading": "ERR",\n'
    rec4 = '{"timestamp": "2026-09-09 10:03:00", "exp_id": "EXP-401", "status": "OK"},\n'
    rec5 = '{"timestamp": "2026-09-09 10:04:00", "exp_id": "EXP-401", "sensor_reading: "ERR", "status": "OK"},\n'
    return rec1, rec2, rec3, rec4, rec5


def test_get_experiment_data(tmp_path, sample_results):
    temp_file = tmp_path / "experiment_results"
    temp_file.write_text(sample_results[0] + sample_results[1], encoding='utf-8')

    gen = get_experiment_data(file_path=temp_file)
    assert next(gen) == sample_results[0]
    assert inspect.getgeneratorstate(gen) == 'GEN_SUSPENDED'
    assert next(gen) == sample_results[1]

    with pytest.raises(StopIteration) as e:
        next(gen)
    assert 'StopIteration' in str(e)


def test_validate_results(sample_results, tmp_path, monkeypatch):
    temp_error_log = tmp_path / "errors.log"

    def mock_log_error(record, file_path=None):
        log_error_records(record, temp_error_log)

    monkeypatch.setattr("pipeline.log_error_records", mock_log_error)

    result_gen = (result for result in sample_results)
    validated_pipeline = validate_results(result_gen)
    valid_result = next(validated_pipeline)
    assert valid_result == json.loads(sample_results[0].strip().rstrip(','))

    remaining_records = list(validated_pipeline)
    assert len(remaining_records) == 0

    assert temp_error_log.exists()

    error_lines = temp_error_log.read_text().splitlines()
    assert len(error_lines) == 4
    assert sample_results[4].strip().rstrip(',') in error_lines


def test_transform_result(sample_results):

    expected_output = {"experiment_id": "EXP-401", "sensor_reading": float(45.2),
                       "timestamp": datetime.strptime("2026-09-09 10:00:00", "%Y-%m-%d %H:%M:%S")}
    result_gen = (result for result in sample_results)
    validated_stream = validate_results(result_gen)
    transformed_stream = transform_result(validated_stream)

    result = next(transformed_stream)
    assert result == expected_output

    remaining_output = list(transformed_stream)
    assert len(remaining_output) == 0


def test_process_stream(sample_results):

    expected_output = {'EXP-401': [1, 45.2, 45.2]}
    result_gen = (result for result in sample_results)
    validated_stream = validate_results(result_gen)
    transformed_stream = transform_result(validated_stream)
    summary = process_stream(transformed_stream)

    assert expected_output == summary
