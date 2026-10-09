import pytest
import numpy as np
from eigen_minicapstone import is_valid_transformation_matrix


def test_is_valid_tranformation_matrix_false_case():
    mat = np.array([[1, 2], [2, 4]])
    assert is_valid_transformation_matrix(mat) is False


def test_is_valid_tranformation_matrix_true_case():
    mat = np.array([[1, 2], [2, 5]])
    assert is_valid_transformation_matrix(mat) is True
