import pytest
import numpy as np
from complex_numbers import complex_magnitude


@pytest.mark.parametrize("value", [
    3.14,
    3,
    "abc",
    [1, 2],
    np.array([[1], [2]]),
    np.array([1, 2]),
])
def test_complex_magnitue_invalid_inputs(value):
    with pytest.raises(ValueError):
        complex_magnitude(value)


@pytest.mark.parametrize("value, expected_output", [
    (3 + 4j, 5),
    (3 - 4j, 5),
    (2 + 0j, 2),
    (0 + 1.5J, 1.5),
    (0 + 0J, 0),
    (-3 - 4j, 5),
])
def test_complex_magnitude_valid_inputs(value, expected_output):
    result = complex_magnitude(value)
    assert result == pytest.approx(expected_output)
