import pytest
from defaultdict_practice import group_by_backend, total_shots_by_backend


@pytest.mark.parametrize("records, output", [
    ([("simulator", 100), ("hardware", 200), ("simulator", 150), ("hardware", 300),],
     {"simulator": [100, 150], "hardware": [200, 300]}),
    ([], {}),
    ([("simulator", 100), ("simulator", 150), ], {"simulator": [100, 150]}),
    ([("simulator", 100),], {"simulator": [100]}),
])
def test_group_by_backend(records, output):
    result = group_by_backend(records)
    assert result == output


@pytest.mark.parametrize("records, output", [
    ([], {}),
    ([("simulator", 100),], {"simulator": 100}),
    ([("simulator", 100), ("simulator", 150), ], {"simulator": 250}),
    ([("simulator", 100), ("hardware", 200), ("simulator", 150), ("hardware", 300), ],
     {"simulator": 250, "hardware": 500}),
])
def test_total_shots_by_backend(records, output):
    result = total_shots_by_backend(records)
    assert result == output
