import pytest
from optimisation_practice import sum_squares_lazy_processing, sum_squares_list_comprehension


@pytest.mark.parametrize("numlist, expected_output", [
    ([1, 2, 3], 14),
    (list(range(5)), 30),
])
def test_list_comprehension(numlist, expected_output):
    result = sum_squares_list_comprehension(numlist)
    assert result == expected_output


@pytest.mark.parametrize("numlist, expected_output", [
    ([1, 2, 3], 14),
    (list(range(5)), 30),
])
def test_lazy_processing(numlist, expected_output):
    result = sum_squares_lazy_processing(numlist)
    assert result == expected_output

