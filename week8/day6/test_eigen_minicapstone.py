import pytest
import numpy as np
from eigen_minicapstone import is_valid_transformation_matrix, get_eigen_values_and_vectors, \
    generate_transformation_matrix, generate_n_sample_vectors, is_transformation_possible


def test_is_valid_tranformation_matrix_false_case():
    mat = np.array([[1, 2], [2, 4]])
    assert is_valid_transformation_matrix(mat) is False


def test_is_valid_tranformation_matrix_true_case():
    mat = np.array([[1, 2], [2, 5]])
    assert is_valid_transformation_matrix(mat) is True


def test_get_eigen_values_and_vectors_identity_matrix():
    """Test a 2x2 Identity Matrix (Eigenvalues should be [1, 1])"""
    matrix = np.array([[1, 0],
                       [0, 1]])

    vals, vecs = get_eigen_values_and_vectors(matrix)

    # Check that eigenvalues are exactly 1
    np.testing.assert_allclose(vals, np.array([1.0, 1.0]))


def test_get_eigen_values_and_vectors_rotation_matrix():
    """Test a 2x2 Identity Matrix (Eigenvalues should be [1, 1])"""
    matrix = np.array([[-1, 0],
                       [0, 1]])

    vals, vecs = get_eigen_values_and_vectors(matrix)

    # Check that eigenvalues are exactly 1
    np.testing.assert_allclose(vals, np.array([-1.0, 1.0]))


@pytest.mark.parametrize("values", [
    -2,
    1,
    3.5,
    "2"
])
def test_generate_transformation_matrix_invalid_values(values):
    with pytest.raises(ValueError):
        generate_transformation_matrix(values)


@pytest.mark.parametrize("values", [
    2,
    3,
    9
])
def test_generate_transformation_matrix_valid_values(values):
    result = generate_transformation_matrix(values)
    assert result.ndim == 2
    assert result.shape == (values, values)


@pytest.mark.parametrize("n, m", [
    (1, 4),
    (4, 1),
    (3.0, 4),
    (-2, -5),
    ("3", "4")
])
def test_generate_n_sample_vectors_invalid_values(n, m):
    with pytest.raises(ValueError):
        generate_n_sample_vectors(n, m)


def test_generate_n_sample_vectors_valid_values():
    result = generate_n_sample_vectors(3, 4)
    assert result.shape == (3, 4)

@pytest.mark.parametrize("matrix, vectors, expected_output", [
    (np.random.rand(3, 3), np.random.rand(3, 2), False),
    (np.random.rand(3, 3), np.random.rand(3, 3), True),
    (np.random.rand(4, 4), np.random.rand(2, 4), True),
    (np.random.rand(4, 4), np.random.rand(4, 3), False),
])
def test_is_transformation_possible(matrix, vectors, expected_output):
    result = is_transformation_possible(matrix, vectors)
    assert result == expected_output
