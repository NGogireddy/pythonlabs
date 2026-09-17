import pytest
import numpy as np
from statistics import calculate_state_statistics


def test_calculate_state_statistics_valueerror_tests():
    with pytest.raises(ValueError):
        calculate_state_statistics(np.array([]))


@pytest.mark.parametrize("values", [
    [1, 2, 3],
    (1, 2),
    'abd',
    np.arange(6).reshape(2, 3),
    np.array(['a', 'b', 'c']),
])
def test_calculate_state_statistics_typeerror_tests(values):
    with pytest.raises(TypeError):
        calculate_state_statistics(values)


@pytest.mark.parametrize("values, expected_output", [
    (np.ones(4), {"count": 4, "mean": 1. , "min": 1, "max": 1}),
    (np.zeros(4), {"count": 4, "mean": 0., "min": 0, "max": 0}),
    (np.arange(4), {"count": 4, "mean": 1.5, "min": 0, "max": 3}),
    (np.array([1.0, 2.0, 3.0]), {"count": 3, "mean": 2.0, "min": 1.0, "max": 3.0}),
])
def test_calculate_state_statistics_valid_inputs(values, expected_output):
    result = calculate_state_statistics(values)
    assert result == expected_output

