import pytest
import numpy as np
from matrix_properties import is_symmetric


@pytest.mark.parametrize("matrix", [
    [[1, 2], [2, 1]],
    np.array([1, 2]),
    np.empty([0]),
    np.array([['a', 'b']]),
    np.array([[1, 2, 3], [4, 5, 6]]),
])
def test_is_symmetric_invalid_inputs(matrix):
    result = is_symmetric(matrix)
    assert result is False


@pytest.mark.parametrize("matrix, expected_result", [
    (np.array([[1]]), True),
    (np.array([[2., 4.4449], [4.4449, 2.]]), True),
    (np.array([[1, -2, 3], [-2, -4, 5], [3, 5, -7]]), True),
    (np.array([[2., 4.4], [4.5, 2.]]), False),
    (np.eye(2), True),
])
def test_is_symmetric_valid_inputs(matrix, expected_result):
    result = is_symmetric(matrix)
    assert result == expected_result
