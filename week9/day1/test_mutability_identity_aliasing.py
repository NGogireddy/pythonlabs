import pytest
from mutability_identity_aliasing import add_sum_to_list


def test_normal_list():
    num_list = [1, 2, 3]
    expected_output = [1, 2, 3, 6]
    result = add_sum_to_list(num_list)
    assert num_list is not result
    assert result == expected_output
    assert id(num_list) is not id(result)


def test_empty_list():
    empty_list = []
    expected_output = [0]
    result = add_sum_to_list(empty_list)
    assert empty_list is not result
    assert result == expected_output
    assert id(empty_list) is not id(result)



