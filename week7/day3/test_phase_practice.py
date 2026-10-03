import pytest
import cmath
import math
import numpy as np
from phase_practice import complex_phase


@pytest.mark.parametrize("value", [
    2.3,
    1,
    "complex number",
    np.array(2 + 4j)
])
def test_complex_phase_invalid_inputs(value):
    with pytest.raises(TypeError):
        complex_phase(value)


@pytest.mark.parametrize("value, expected_output", [
    (0 + 0j, 0),
    (1 + 0j, 0),
    (1 + 1j, 45),
    (0 + 1j, 90),
    (-1 + 1j, 135),
    (-1 + 0j, 180),
    (-1 - 1j, -135),
    (0 - 1j, -90),
    (1 - 1j, -45),
])
def test_complex_phase_valid_inputs(value, expected_output):
    result = complex_phase(value)
    assert math.isclose(result, expected_output)


def test_complex_phase_polar_input():
    r = 5
    # Convert 53.13 degrees to radians
    theta = math.radians(53.13)

    # Initialize using rect(magnitude, angle_in_radians)
    z = cmath.rect(r, theta)

    result = complex_phase(z)
    assert math.isclose(result, 53.13)
