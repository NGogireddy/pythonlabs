import pytest
from counter_practice import count_states, get_most_common


@pytest.mark.parametrize("states, counts", [
    ([2, 3, 4, 2, 1, 3], {2: 2, 3: 2, 4: 1, 1: 1}),
    ([], {}),
    (['abc', 1], {'abc': 1, 1: 1})
])
def test_count_states(states, counts):
    output = count_states(states)
    assert output == counts


@pytest.mark.parametrize("states, output", [
    ([2, 3, 4, 2], 2),
    ([2, 3, 2, 3], 2),
    ([3, 2, 3, 2], 3),
    ([], None)
])
def test_get_most_common(states, output):
    result = get_most_common(states)
    assert result == output
