import pytest
import numpy as np
from matrix_multiplication import multiply_matrices


@pytest.mark.parametrize("left, right", [
    ([1, 2], [2, 1]),
    (np.array([1, 2]), np.array([2, 1])),
    (np.array([1, 2]), [[2], [1]]),
    ([[2], [1]], np.array([1, 2])),
    (np.array(['1', '2']), np.array([['1'], ['2']])),
    (np.array([['1'], ['2']]), np.array(['1', '2'])),
    (np.empty([0]), np.empty([0])),
])
def test_multiply_matrices_invalid_inputs(left, right):
    result = multiply_matrices(left, right)
    assert result is None


@pytest.mark.parametrize("left, right, expected_output", [
    (np.array([[1, 2]]), np.array([[2], [1]]), 4),
    (np.array([[1, 2], [2, 1]]), np.array([[1, 0], [0, 1]]), np.array([[1, 2], [2, 1]])),
    (np.array([[1, 2, 3], [4, 5, 6]]), np.array([[1, 2], [3, 4], [5, 6]]), np.array([[22, 28], [49, 64]])),
    (np.array([[1., 2.], [2., 1.]]), np.array([[1., 0.], [0., 1.]]), np.array([[1., 2.], [2., 1.]])),
    (np.array([[1., -2.], [2., 1.]]), np.array([[1., -1.], [0., 1.]]), np.array([[1., -3.], [2., -1.]])),
])
def test_multiply_matrices_valid_inputs(left, right, expected_output):
    result = multiply_matrices(left, right)
    np.testing.assert_allclose(result, expected_output)
