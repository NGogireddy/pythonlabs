import pytest
import numpy as np
from array_practice import describe_array


@pytest.mark.parametrize("values", [
    "abc",
    [1, 2],
    3.4,
    {2, 3, 4},
    {1: 2, 'a':'b'},
])
def test_describe_array_invalid_input(values):
    with pytest.raises(TypeError):
        describe_array(values)


@pytest.mark.parametrize("values, output", [
    (np.arange(4), {"shape": (4, ), "ndim": 1, "size": 4, "dtype": 'int64'}),
    (np.arange(4).reshape(2, 2), {"shape": (2, 2), "ndim": 2, "size": 4, "dtype": 'int64'}),
    (np.array([]), {"shape": (0, ), "ndim": 1, "size": 0, "dtype": 'float64'}),
])
def test_describe_array_valid_input(values, output):
    result = describe_array(values)
    assert result == output
