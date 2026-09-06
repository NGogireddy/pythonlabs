import pytest
from generator_practice import is_valid_result, generate_valid_results


@pytest.mark.parametrize("result, output", [
    ({"experiment_id": "str", "state": "str", "count": 10}, True),
    ({"experiment_id": "str", "state": "str"}, False),
    ({"experiment_id": "str", "count": 10}, False),
    ({"state": "str", "count": 10}, False),
    ({"experiment_id": 1, "state": "str", "count": 10}, False),
    ({"experiment_id": "str", "state": {1:1}, "count": 10}, False),
    ({"experiment_id": "str", "state": "str", "count": "10"}, False),
])
def test_is_valid_result(result, output):
    result = is_valid_result(result)
    assert result == output


@pytest.mark.parametrize("results, output", [
    ([], []),
    ([
        {"experiment_id": "abc", "state": "completed", "count": 10},
        {"experiment_id": "def", "state": "completed", "count": 15},
    ], [
        {"experiment_id": "abc", "state": "completed", "count": 10},
        {"experiment_id": "def", "state": "completed", "count": 15},
    ]),
    ([
         {"experiment_id": "abc", "state": "completed", "count": 10},
         {"experiment_id": "def", "state": "completed", "count": "15"},
     ], [
         {"experiment_id": "abc", "state": "completed", "count": 10},
     ]),
    ([
         {"experiment_id": "abc", "state": {1:1}, "count": 10},
         {"experiment_id": (), "state": "completed", "count": 15},
     ], [
     ]),

])
def test_generate_valid_results(results, output):
    result = []
    gen = generate_valid_results(results)
    for item in gen:
        result.append(item)
    assert result == output


def test_generate_valid_results_behaviour():
    results = [
        {"experiment_id": "abc", "state": "completed", "count": 10},
        {"experiment_id": "def", "state": "completed", "count": 15},
    ]
    output1 = {"experiment_id": "abc", "state": "completed", "count": 10}
    output2 = {"experiment_id": "def", "state": "completed", "count": 15}

    gen = generate_valid_results(results)
    result1 = next(gen)
    assert result1 == output1

    result2 = next(gen)
    assert result2 == output2
