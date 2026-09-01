import pytest
import time
from permutations_practice import get_permutations


@pytest.mark.parametrize("qubits, length, output", [
    (['q0', 'q1', 'q2'], 3, [('q0', 'q1', 'q2'), ('q0', 'q2', 'q1'), ('q1', 'q0', 'q2'), ('q1', 'q2', 'q0'), ('q2', 'q0', 'q1'), ('q2', 'q1', 'q0')]),
    (['q0', 'q1', 'q2'], 2, [('q0', 'q1'), ('q0', 'q2'), ('q1', 'q0'), ('q1', 'q2'), ('q2', 'q0'), ('q2', 'q1')]),
    (['q0', 'q1', 'q2'], 1, [('q0',), ('q1',), ('q2',)]),
    (['q0', 'q1', 'q2'], None, [('q0', 'q1', 'q2'), ('q0', 'q2', 'q1'), ('q1', 'q0', 'q2'), ('q1', 'q2', 'q0'), ('q2', 'q0', 'q1'), ('q2', 'q1', 'q0')]),
    (['q0', 'q1', 'q2'], 4, []),
    ([], 3, None),
])
def test_get_permutations(qubits, length, output):
    result = get_permutations(qubits, length)
    assert result == output


def test_get_permutations_performance():
    start_time = time.perf_counter()
    result = get_permutations(range(5), 5)
    end_time = time.perf_counter()
    print(f'Time for getting permutations of 5 items {end_time - start_time}')

    start_time = time.perf_counter()
    result = get_permutations(range(10), 10)
    end_time = time.perf_counter()
    print(f'Time for getting permutations of 10 items {end_time - start_time}')
