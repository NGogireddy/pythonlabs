import pytest
import numpy as np
from complex_amplitude_analyses import complex_analyses


@pytest.mark.parametrize("values", [
    [1+2j, 3+4j],
    np.array([1, 2, 3]),
    np.array([[1+2j, 3+4j]]),
])
def test_invalid_inputs(values):
    with pytest.raises(TypeError):
        complex_analyses(values)


@pytest.mark.parametrize("values, expected_output", [
    (np.array([3 + 4j]), {'magnitudes': np.array([5.]),
     'normalised_vector': np.array([0.6 + 0.8j]),
     'probabilities': np.array([1.])}),
    (np.array([3 + 4j, 10 - 6j, -2 + 2j]), {'magnitudes': np.array([5., 11.661903, 2.828427]),
                          'normalised_vector': np.array([0.23076923 + 0.3067923076j, 0.76923076923 - 0.46153846153j, -0.153846153846 + 0.153846153846j]),
                          'probabilities': np.array([0.14792899, 0.8047337, 0.047337])}),
    (np.empty(0, dtype=complex), {'magnitudes': np.empty(0, dtype=float),
               'normalised_vector': np.empty(0, dtype=complex),
               'probabilities': np.empty(0, dtype=complex)}),
])
def test_valid_inputs(values, expected_output):
    result = complex_analyses(values)
    np.testing.assert_allclose(result['magnitudes'], expected_output['magnitudes'], atol=1e-3)
    np.testing.assert_allclose(result['normalised_vector'], expected_output['normalised_vector'], atol=1e-3)
    np.testing.assert_allclose(result['probabilities'], expected_output['probabilities'], atol=1e-3)
