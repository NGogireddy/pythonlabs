import pytest
import numpy as np
from vector_operations import vector_dot_product


@pytest.mark.parametrize("a, b, expected_error", [
    (np.array(['a', 'b']), np.array([1, 2]), "A array is not "),
    (np.array([1, 2]), np.array(['1', '2']), "B array is not "),
    (np.array(['a', 'b']), np.array(['1', '2']), "A array is not "),
    ([1, 2], np.array([1, 2]), "A array is not "),
    (np.array([1, 2]), [1, 2], "B array is not "),
    (np.array([[1, 2], [3, 4]]), np.array([1, 2]), "A array is not "),
    (np.array([1, 2]), np.array([[1, 2], [3, 4]]), "B array is not "),
    (np.array([1, 2]), np.array([1, 2, 3]), "not of same size"),
])
def test_vector_dot_product_error_scenarios(a, b, expected_error):
    with pytest.raises(ValueError) as e:
        vector_dot_product(a, b)
    assert expected_error in str(e.value)


@pytest.mark.parametrize("a, b, expected_output", [
    (np.array([1, 2]), np.array([1, 2]), 5),
    (np.array([1., 2.]), np.array([1, 2]), 5.),
    (np.array([-1., -2.]), np.array([1, 2]), -5.),
    (np.empty([0]), np.empty([0]), 0),
])
def test_vector_dot_product_valid_scenarios(a, b, expected_output):
    result = vector_dot_product(a, b)
    assert result == expected_output
