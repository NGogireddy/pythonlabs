import pytest
import math
import numpy as np
from trigonometry_practice import unit_complex_from_phase


@pytest.mark.parametrize("rad", [
    "abd",
    1 + 2j,
    [45],
    math.nan,
    math.inf,
])
def test_invalid_inputs(rad):
    result = unit_complex_from_phase(rad)
    np.testing.assert_allclose(result, complex(0, 0))


@pytest.mark.parametrize("rad, expected_output", [
    (0, complex(1, 0)),
    (np.pi, complex(-1, 0)),
    (np.pi*2, complex(1, 0)),
    (np.pi/2, complex(0, 1)),
    (np.pi * 3/2, complex(0, -1)),
    (-np.pi/2, complex(0, -1)),
    (-np.pi, complex(-1, 0)),
])
def test_valid_inputs(rad, expected_output):
    result = unit_complex_from_phase(rad)
    np.testing.assert_allclose(result, expected_output)
