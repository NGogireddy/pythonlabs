import pytest
import numpy as np
from eigen_vectors_practice import get_eigen_values


@pytest.mark.parametrize("values", [
    [[1, 2], [3, 4]],
    np.array([['1', '2'], ['3', '4']]),
    np.array([1, 2]),
    np.array([[1, 2, 3], [4, 5, 6]]),
    np.array([[[1, 2, 3], [4, 5, 6]],
              [[1, 2, 3], [4, 5, 6]],
              [[1, 2, 3], [4, 5, 6]]]),
])
def test_invalid_inputs(values):
    result = get_eigen_values(values)
    assert result is None


@pytest.mark.parametrize("values", [
    np.array([[3, 2], [2, 3]]),
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
])
def test_valid_input(values):
    result = get_eigen_values(values)
    eigen_values = result[0]
    eigen_vectors = result[1]

    for num in range(len(eigen_values)):
        vector = eigen_vectors[:, num]
        lhs = values @ vector
        rhs = eigen_values[num] * vector
        np.testing.assert_allclose(lhs, rhs, atol=1e-7)
