import pytest
import numpy as np
from main import read_experiment_results, convert_exp_numpy, is_valid_experiment, convert_to_nparray, \
    process_experiment, process_results


@pytest.fixture
def sample_results():
    rec1 = 'np.array([0.1, 0.2, 0.3, 0.4]),\n'
    rec2 = 'np.array([0.7, 0.8, np.nan]),\n'
    return rec1, rec2


def test_read_experiment_results(tmp_path, sample_results):
    tmp_file = tmp_path / "experiment_results"
    tmp_file.write_text(sample_results[0] + sample_results[1], encoding='utf-8')

    gen = read_experiment_results(tmp_file)
    assert next(gen) == sample_results[0].strip(',\n')
    assert next(gen) == sample_results[1].strip(',\n')

    with pytest.raises(StopIteration):
        next(gen)


def test_convert_exp_numpy_invalid_inputs():
    exp_results = [
        "[0.7, 0.8, 0.9]",
        "(0.7, 0.8, 0.9)",
        "np.array(['a', 'b'])",
        "np.array([[1, 2], [3, 4]])",
    ]
    gen = convert_exp_numpy(exp_results)
    for result in gen:
        assert result.size == 0


@pytest.mark.parametrize("exp_results, expected_output", [
    (["np.array([1, np.nan])"], np.array([1, np.nan])),
    (["np.array([1.0, 2.0, 3.0])"], np.array([1.0, 2.0, 3.0])),
    (["np.array([0])"], np.array([0])),
])
def test_convert_exp_numpy_valid_inputs(exp_results, expected_output):
    gen = convert_exp_numpy(exp_results)
    for result in gen:
        np.testing.assert_array_equal(result, expected_output)


@pytest.mark.parametrize("experiments", [
    "[0.7, 0.8, 0.9]",
    "(0.7, 0.8, 0.9)",
    "stringtest",
    "np.array([[0.1], [0.2], [0.3]])",
    "np.array(['0.0', '-0.8', '0.9'])",
    "np.array([1, 2, 3]",
])
def test_is_valid_experiment_invalid_experiments(experiments):
    result = is_valid_experiment(experiments)
    assert result is False


@pytest.mark.parametrize("experiments", [
    "np.array([0.1, 0.2, 0.3])",
    "np.array([1, 2, 3])",
    "np.empty([0])",
])
def test_is_valid_experiment_valid_experiments(experiments):
    result = is_valid_experiment(experiments)
    assert result is True


@pytest.mark.parametrize("experiment, expected_output", [
    ("np.array([1, np.nan])", np.array([1, np.nan])),
    ("np.array([1.0, 2.0, 3.0])", np.array([1.0, 2.0, 3.0])),
    ("np.array([0])", np.array([0])),
])
def test_convert_to_nparray_valid_inputs(experiment, expected_output):
    result = convert_to_nparray(experiment)
    np.testing.assert_array_equal(result, expected_output)

