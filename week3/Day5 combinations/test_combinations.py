import pytest
from combinations_practice import get_unique_combinations


@pytest.mark.parametrize("inputs, length, output", [
    (range(4), 2, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]),
    (range(4), 3, [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]),
    (range(4), None, [(0,), (1,), (2,), (3,)]),
    (range(4), 0, [()]),
    (range(4), 5, []),
])
def test_get_unique_combinations(inputs, length, output):
    result = get_unique_combinations(inputs, length)
    assert result == output


def test_get_unique_combinations_negative_length():
    with pytest.raises(ValueError) as e:
        get_unique_combinations(range(2), -1)
    assert 'length must be a positive integer' in str(e.value)


def test_get_unique_combinations_floating_length():
    with pytest.raises(ValueError) as e:
        get_unique_combinations(range(3), 2.5)
    assert 'length must be a positive integer' in str(e.value)
