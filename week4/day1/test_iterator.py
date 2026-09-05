import pytest
from iterator_practice import consume_first_n, InputError


@pytest.mark.parametrize("iterable, n, output", [
    (iter([1, 2, 3, 4]), 2, [1, 2]),
    (iter((1, 2, 3, 4)), 2, [1, 2]),
    (iter({1, 2, 3, 4}), 2, [1, 2]),
    (iter("1234"), 2, ["1", "2"]),
    (iter("1234"), -2, []),
    (iter({"a0": 0, "a1": 1}), 1, ["a0"]),
    (iter([]), 0, []),
])
def test_consume_first_n_positive_cases(iterable, n, output):
    result = consume_first_n(iterable, n)
    assert result == output


@pytest.mark.parametrize("iterable, n, message", [
    ([1, 2, 3], 2, "object is not an iterator"),
    (iter([]), 1, "Requested items more than iterable contents"),
])
def test_consume_first_n_exception_cases(iterable, n, message):
    with pytest.raises(InputError) as e:
        consume_first_n(iterable, n)
    assert message in str(e.value)
