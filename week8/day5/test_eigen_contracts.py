import pytest
import numpy as np
from eigen_contracts import is_valid_matrix, calculate_eigen_values


@pytest.mark.parametrize("values", [
    [[1, 2], [3, 4]],
    np.array([1, 2]),
    np.array([['1', '2'], ['3', '4']]),
    np.array([[1, 2, 3], [4, 5, 6]])
])
def test_is_valid_matrix_invalid_input(values):
    assert is_valid_matrix(values) is False


@pytest.mark.parametrize("values", [
    np.array([[1, 2], [3, 4]]),
    np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]]),
    np.array([[[1, 2, 3], [3, 4, 5], [4, 5, 6]],
              [[1, 2, 3], [3, 4, 5], [4, 5, 6]]]),
])
def test_is_valid_matrix_valid_input(values):
    assert is_valid_matrix(values) is True


@pytest.mark.parametrize("values", [
    np.array([[3, 2], [2, 3]]),  # 2D case
    np.random.rand(2, 3, 3),  # 3D Batch case
    np.random.rand(4, 2, 3, 3),  # 4D Batch case
])
def test_valid_input(values):
    result = calculate_eigen_values(values)
    assert result is not None

    eigen_values, eigen_vectors = result

    # ONE-LINE VALIDATION FOR ALL DIMENSIONS
    np.testing.assert_allclose(
        values @ eigen_vectors,
        eigen_vectors * eigen_values[..., np.newaxis, :],
        atol=1e-7
    )
