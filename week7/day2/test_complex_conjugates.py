import pytest
import numpy as np
from complex_conjugates import conjugate_vectors


@pytest.mark.parametrize("values", [
    np.array([[2 + 1j]]),
    np.empty(0, dtype=complex),
    np.array([2, 3]),
    [2 + 3j, 1 - 4j],
    [1, 2, 3],
])
def test_conjugate_vectors_invalid_inputs(values):
    with pytest.raises(TypeError):
        conjugate_vectors(values)


@pytest.mark.parametrize("values, expected_output", [
    (np.array([1 + 2j, 3 - 4j]), np.array([1 - 2j, 3 + 4j])),
    (np.empty(1, dtype=complex), np.array(0 - 0j)),
    (np.array([1 + 0j]), np.array([1 - 0j])),
])
def test_conjugate_vectors_valid_inputs(values, expected_output):
    result = conjugate_vectors(values)
    np.testing.assert_allclose(result, expected_output)
