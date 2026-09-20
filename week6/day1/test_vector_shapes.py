import pytest
import numpy as np
from vector_shapes import describe_vector


@pytest.mark.parametrize("values", [
    np.array([[1, 2, 3]]),
    np.array(['1', '2',]),
    [1, 2, 3],
    (1, 2, 3),
    "123",
    np.empty([0]),
    np.array(2)
])
def test_describe_vector_invalid_values(values):
    output = {"length": 0, "shape": 0, "dtype": "" }
    result = describe_vector(values)
    assert result == output


@pytest.mark.parametrize("values, expected_output", [
    (np.array([1, -2, 3]), {"length": 3, "shape": (3, ), "dtype": "int64"}),
    (np.array([1.0, 2.0]), {"length": 2, "shape": (2, ), "dtype": "float64"}),
])
def test_describe_vector_valid_values(values, expected_output):
    result = describe_vector(values)
    assert result == expected_output
