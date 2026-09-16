import pytest
import numpy as np
from aggregation import column_statistics


"Tests for empty arrays, invalid dimensionality, and non-numeric data"
@pytest.mark.parametrize("matrix", [
    np.arange(18).reshape(2, 3, 3),
    np.array([['a', 'b'], ['c', 'd']], dtype='U'),
])
def test_column_statistics_None_output(matrix):
    result = column_statistics(matrix)
    assert result is None


def test_column_statistics_empty_arrays():
    arr = np.array([])
    result = column_statistics(arr)
    assert result is None


def test_column_statistics_zero_row_arrays():
    zero_matrix = np.empty((0, 2))
    expected_output = np.array([np.nan, np.nan])
    result = column_statistics(zero_matrix)
    np.testing.assert_array_equal(result, expected_output)


def test_column_statistics_one_row():
    one_row = np.array([1, 2, 3])
    expected_output = np.array([2.])
    result = column_statistics(one_row)
    np.testing.assert_array_equal(result, expected_output)


def test_column_statistics_one_column():
    one_column = np.array([[1], [2], [3]])
    expected_output = np.array([2.])
    result = column_statistics(one_column)
    np.testing.assert_array_equal(result, expected_output)


def test_column_statistics_negative_numbers():
    neg_matrix = np.array([[-1], [-2], [-3]])
    expected_output = np.array([-2.])
    result = column_statistics(neg_matrix)
    np.testing.assert_array_equal(result, expected_output)


def test_column_statistics_2d_matrix():
    matrix = np.array([[1, 2, 3], [5, 6, 7]])
    expected_output = np.array([3., 4., 5.])
    result = column_statistics(matrix)
    np.testing.assert_array_equal(result, expected_output)

