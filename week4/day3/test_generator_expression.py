import pytest
from generator_expression_practice import get_valid_counts, sum_valid_counts


@pytest.mark.parametrize("results, output", [
    ([
        {"experiment_id": "abc", "state": "completed", "count": 10},
        {"experiment_id": "def", "state": "completed", "count": 15},
    ], [10, 15]),
    ([
         {"experiment_id": "abc", "state": "completed", "count": 10},
         {"experiment_id": "def", "state": "completed", "counts": 15},
     ], [10]),
    ([], []),
    ([
         {"experiment_id": "abc", "state": "completed", "count": -3},
         {"experiment_id": "def", "state": "completed", "counts": 15},
         {"experiment_id": "abc", "states": "completed", "count": 10},
         {"experiment_ids": "def", "state": "completed", "count": 15},
         {"experiment_id": "abc", "state": "completed", "count": -3},
         {"experiment_id": "def", "state": "completed"},
     ], []),
])
def test_get_valid_counts(results, output):
    result_list = [count for count in get_valid_counts(results)]
    assert result_list == output


@pytest.mark.parametrize("results, output", [
    ([
         {"experiment_id": "abc", "state": "completed", "count": 10},
         {"experiment_id": "def", "state": "completed", "count": 15},
     ], 25),
    ([
         {"experiment_id": "abc", "state": "completed", "count": 10},
         {"experiment_id": "def", "state": "completed", "counts": 15},
     ], 10),
    ([], 0),
    ([
         {"experiment_id": "abc", "state": "completed", "count": -3},
         {"experiment_id": "def", "state": "completed", "counts": 15},
         {"experiment_id": "abc", "states": "completed", "count": 10},
         {"experiment_ids": "def", "state": "completed", "count": 15},
         {"experiment_id": "abc", "state": "completed", "count": -3},
         {"experiment_id": "def", "state": "completed"},
     ], 0),

])
def test_sum_valid_counts(results, output):
    result = sum_valid_counts(results)
    assert result == output
