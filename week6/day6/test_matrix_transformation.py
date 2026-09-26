import pytest
import numpy as np
from matrix_transformation import is_compatible, is_valid, transform_vectors, collect_transformed_vectors, \
    transform_vectors_alternative
from unittest.mock import patch


@pytest.mark.parametrize("arr", [
    [1, 2],
    np.array(['a', 'b']),
    "invalid_array",
])
def test_is_valid_invalid_inputs(arr):
    assert is_valid(arr) is False


@pytest.mark.parametrize("arr", [
    np.empty([0]),
    np.array([1, 2, 3]),
    np.arange(9).reshape(3, 3),
])
def test_is_valid_valid_inputs(arr):
    assert is_valid(arr)


@pytest.mark.parametrize("mat_shape, vec_shape, expected_output", [
    ((2, 2), (2,), True),
    ((2, 2), (2, 2), True),
    ((2, 2), (2, 3), False),
    ((3, 2), (2, 2), False),
    ((1, 1), (1, ), True),
    ((1, 1, 1), (1,), False),
    ((1, ), (1, 1), False),
])
def test_is_compatible(mat_shape, vec_shape, expected_output):
    result = is_compatible(mat_shape, vec_shape)
    assert result == expected_output


def test_transform_vectors_one_vector():
    matrix = np.array([[1, 2], [3, 4]])
    vector = np.array([1, 0])
    expected_result = np.array([1, 3])
    stream = transform_vectors(matrix, vector)
    np.testing.assert_allclose(next(stream), expected_result)


def test_transform_vectors_two_vectors():
    matrix = np.array([[1, 2], [3, 4]])
    vector = np.array([[1, 0], [0, 1]])
    expected_result = np.array([[1, 3], [2, 4]])
    stream = transform_vectors(matrix, vector)
    for result in expected_result:
        np.testing.assert_allclose(next(stream), result)


def test_collect_transformed_vectors():
    """Test that the function correctly collects items yielded by the stream."""
    # Mock inputs
    mock_matrix = np.array([[1, 2], [3, 4]])
    mock_vectors = np.array([[1, 0], [0, 1]])

    # Expected output from the generator stream
    mock_stream_output = [np.array([1, 3]), np.array([2, 4])]

    # Patch 'transform_vectors' where it is imported/used in vector_utils
    with patch('matrix_transformation.transform_vectors') as mock_transform:
        # Make the mock function return an iterable/generator
        mock_transform.return_value = iter(mock_stream_output)

        # Call the function under test
        result = collect_transformed_vectors(mock_matrix, mock_vectors)

        # Assertions
        mock_transform.assert_called_once_with(mock_matrix, mock_vectors)
        assert len(result) == len(mock_stream_output)
        np.testing.assert_allclose(result[0], mock_stream_output[0])
        np.testing.assert_allclose(result[1], mock_stream_output[1])


def test_transform_vectors_alternative_one_vectors():
    matrix = np.array([[1, 2], [3, 4]])
    vectors = np.array([1, 0])
    expected_output = np.array([1, 3])

    result = transform_vectors_alternative(matrix, vectors)
    np.testing.assert_allclose(result, expected_output)


def test_transform_vectors_alternative_multiple_vectors():
    matrix = np.array([[1, 2], [3, 4]])
    vectors = np.array([[1, 0], [0, 1]])
    expected_output = np.array([[1, 3], [2, 4]])

    result = transform_vectors_alternative(matrix, vectors)
    np.testing.assert_allclose(result, expected_output)
