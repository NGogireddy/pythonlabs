import pytest
import numpy as np
from linear_systems import solve_linear_system


@pytest.mark.parametrize("matrix, vector", [
    (np.array([['1', '2'], ['3', '4']]), np.array([1, 1])),
    (np.array([[1, 2], [3, 4]]), np.array(['1', '1'])),
    (np.array([1, 2]), np.array([1, 2])),
    ([1, 2], np.array([1, 2])),
    (np.array([[1, 2], [3, 4]]), [1, 2]),
    (np.array([[1, 2], [3, 4]]), np.array([[1, 2], [3, 4]])),
    (np.array([[1, 2], [3, 4], [5, 6]]), np.array([[1, 2]])),
    (np.array([[1, 2], [3, 4]]), np.array([1])),
    (np.array([[4, 2], [2, 1]]), np.array([8, 4])),
])
def test_solve_linear_system_invalid_inputs(matrix, vector):
    result = solve_linear_system(matrix, vector)
    assert result is None


@pytest.mark.parametrize("matrix, vector, expected_result", [
    (np.array([[2, 1], [1, -1]]), np.array([5, 1]), np.array([2, 1])),
    (np.array([[2, -1, 3], [3, 1, -1], [1, 2, 1]]), np.array([11, 8, 7]), np.array([3, 1, 2])),
    (np.eye(3), np.array([11, 8, 7]), np.array([11, 8, 7])),
])
def test_solve_linear_system_valid_inputs(matrix, vector, expected_result):
    result = solve_linear_system(matrix, vector)
    np.testing.assert_allclose(result, expected_result)
