import pytest
import numpy as np
from vectorisation import normalise_values


@pytest.mark.parametrize("values, min, max, output", [
    (np.array(range(6)), 0, 5, np.array([0., 0.2, 0.4, 0.6, 0.8, 1.])),
    (np.array(range(3)), 1, 2, np.array([-1., 0, 1.])),
    (np.array([0.5, 1.0, 1.5]), 0.5, 1.5, np.array([0., 0.5, 1.])),
    (np.arange(6).reshape(2, 3), 1, 2, None),
    (np.array(range(3)), 1, 1, None),
    (np.array(range(3)), 2, 1, None),
    (np.array([]), 1, 2, None),
    ([1, 2, 3], 1, 2, None),
])
def test_normalise_values_valid_input(values, min, max, output):
    result = normalise_values(values, min, max)
    np.testing.assert_array_equal(result, output)
