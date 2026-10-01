import pytest
import numpy as np
from normalize_complex_vectors import normalized_vector


@pytest.mark.parametrize("values", [
    [1+2j, 3+4j],
    np.array([1, 2, 3]),
    np.array([[1+2j, 3+4j]]),
    np.empty(0, dtype='complex128')
])
def test_invalid_inputs(values):
    with pytest.raises(TypeError):
        normalized_vector(values)


@pytest.mark.parametrize("values, expected_output", [
    (np.array([3 + 0j, 4 + 0j]), np.array([0.6 + 0j, 0.8 + 0j])),
    (np.array([3 + 4j]), np.array([0.6 + 0.8j])),
    (np.array([0 + 0j]), np.array([0 + 0j])),
    (np.array([0 + 0j, 0 + 0j]), np.array([0 + 0j, 0 + 0j])),
    (np.array([3 - 4j, 0 + 0j]), np.array([0.6 - 0.8j, 0 + 0j])),
    (np.array([0 + 4j, 0 - 3j]), np.array([0 + 0.8j, 0 - 0.6j])),
])
def test_valid_inputs(values, expected_output):
    result = normalized_vector(values)
    np.testing.assert_allclose(result, expected_output)


def test_modification_to_original_values():
    values = np.array([3 - 4j, 0 + 0j])
    values_copy = values.copy()
    _ = normalized_vector(values)
    np.testing.assert_allclose(values, values_copy)
