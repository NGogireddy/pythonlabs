import pytest
from iteration_tools import pair_results, first_n_results


@pytest.mark.parametrize("states, counts, output", [
    ([], [], []),
    (['01', '10'], [100, 98], [('01', 100), ('10', 98)]),
    (['01', '10', '11', '00'], [100, 98], [('01', 100), ('10', 98)]),
    (['01', '10'], [100, 98, 102, 100], [('01', 100), ('10', 98)]),
    (['01', '10'], [], []),
    ([], [100, 98], []),
])
def test_pair_results(states, counts, output):
    result = pair_results(states, counts)
    assert result == output


def generate_more_numbers(limit=5):
    for i in range(limit):
        yield i


@pytest.mark.parametrize("n, output", [
    (0, []),
    (4, [0, 1, 2, 3]),
    (7, [0, 1, 2, 3, 4])
])
def test_first_n_results(n, output):
    result = first_n_results(generate_more_numbers(), n)
    assert result == output
