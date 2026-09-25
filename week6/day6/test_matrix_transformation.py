import pytest
import numpy as np
from matrix_transformation import is_compatible, is_valid, transform_vectors, collect_transformed_vectors


@pytest.mark.parametrize("arr", [
    [1, 2],
    np.array(['a', 'b']),
    "invalid_array",
])
def test_is_valid_invalid_inputs(arr):
    assert is_valid(arr) is False


@pytest.mark.parametrize("arr", [
    np.empty([0]),
    np.array([1, 2, 3]),
    np.arange(9).reshape(3, 3),
])
def test_is_valid_valid_inputs(arr):
    assert is_valid(arr)


@pytest.mark.parametrize("mat_shape, vec_shape, expected_output", [
    ((2, 2), (2,), True),
    ((2, 2), (2, 2), True),
    ((2, 2), (2, 3), False),
    ((3, 2), (2, 2), False),
    ((1, 1), (1, ), True),
    ((1, 1, 1), (1,), False),
    ((1, ), (1, 1), False),
])
def test_is_compatible(mat_shape, vec_shape, expected_output):
    result = is_compatible(mat_shape, vec_shape)
    assert result == expected_output
