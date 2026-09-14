import pytest
import numpy as np
from slicing_practice import first_n_rows


@pytest.mark.parametrize("matrix, rows", [
    ([1, 2], 1),                        # not a numpy matrix
    (np.array([1, 2]), 1),              # 1d array
    (np.array([[1, 2], [3, 4]]), -1),   # rows is negative
    (np.array([[1, 2], [3, 4]]), 0.5),  # floating input
    (np.array([[1, 2], [3, 4]]), 1.0),  # floating input instead of int
    (np.array([[[1, 2], [3, 4]]]), 1),  # 3d matrix
])
def test_first_n_rows_invalid_input(matrix, rows):
    with pytest.raises(TypeError):
        first_n_rows(matrix, rows)


@pytest.mark.parametrize("matrix, rows, output", [
    (np.array([[1, 2], [3, 4]]), 1, np.array([[1, 2]])),  # get 1 row
    (np.array([[1, 2], [3, 4]]), 2, np.array([[1, 2], [3, 4]])),  # get both rows
    (np.array([[1, 2], [3, 4]]), 3, np.array([[1, 2], [3, 4]])),  # get all rows
    (np.array([[1, 2], [3, 4]]), 0, np.empty((0, 2), dtype='int64')),  # get nothing
])
def test_first_n_rows_valid_input(matrix, rows, output):
    result = first_n_rows(matrix, rows)
    np.testing.assert_array_equal(result, output)
