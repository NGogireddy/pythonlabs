import pytest
from pathlib import Path
from capstone3 import is_valid_result, get_file_path, get_results, process_result, InvalidResultError, summary


@pytest.fixture()
def clean_summary_global():
    summary.clear()
    yield
    summary.clear()


@pytest.mark.parametrize("result", [
    {"state": 0, "count": 78},
    {"state": '0', "count": '23'},
    {"states": '0', "count": 78},
    {"state": '0', "counts": 78},
])
def test_is_valid_result_exceptions(result):
    with pytest.raises(InvalidResultError) as e:
        is_valid_result(result)
    assert "Not a valid result" in str(e.value)


def test_is_valid_result_true():
    test_result = {"state": '00', "count": 20}
    assert is_valid_result(test_result)


def test_get_file_path(monkeypatch):
    fake_script_path = Path("/fake/dir/script.py")
    monkeypatch.setattr(Path, "resolve", lambda self: fake_script_path)
    result = get_file_path()
    assert result == Path("/fake/dir/results")


def test_get_results(tmp_path):
    tmp_file = tmp_path / "results"
    data = '[{"state": "00", "count": 482}, {"state": "11", "count": 498}, {"state": "01", "count": 12},]'
    tmp_file.write_text(data, 'utf-8')

    result = get_results(tmp_file)
    assert result == data


def test_process_results_once(clean_summary_global):
    test_result = {"state": "ab", "count": 482}
    process_result(test_result)

    assert summary["ab"] == 482


def test_process_results_twice(clean_summary_global):
    test_result1 = {"state": "ab", "count": 482}
    test_result2 = {"state": "ab", "count": 10}
    process_result(test_result1)
    process_result(test_result2)

    assert summary["ab"] == 492
