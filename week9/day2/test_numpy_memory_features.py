import pytest
import numpy as np
from numpy_memory_features import return_first_n_rows


@pytest.mark.parametrize("array, rows", [
    (np.empty((0, 2)), 2),
    (np.array([1, 2]), 2),
    (np.random.rand(3, 3, 3), 2),
    ([[1, 2], [3, 4]], 1),
    (np.random.rand(2, 2), -1),
    (np.random.rand(2, 2), 0),
    (np.random.rand(2, 2), 'a'),
    (np.random.rand(2, 2), 3+1.2j),
])
def test_invalid_inputs(array, rows):
    result = return_first_n_rows(array, rows)
    assert result.size == 0
    assert result.shape == (0, 2)


@pytest.mark.parametrize("array, rows", [
    (np.array([[1, 2, 3], [4, 5, 6]]), 1),
    (np.array([[1, 2, 3], [4, 5, 6]]), 2),
    (np.array([[1, 2, 3], [4, 5, 6]]), 3),
])
def test_valid_inputs(array, rows):
    result = return_first_n_rows(array, rows)
    np.testing.assert_allclose(result, array[0:rows])
    assert not np.shares_memory(array, result)
