import numpy as np
import pytest
from npbasics import manipulate_array_memory


@pytest.mark.parametrize("arr, change, ownership", [
    (np.array(range(4)), True, False),
    (np.array([range(3), range(3,6)]), True, False),
    (np.array(range(4)), False, True),
    (np.array([range(3), range(3, 6)]), False, True),
])
def test_manipulate_array_memory(arr, change, ownership):
    result = manipulate_array_memory(arr, change)
    assert result.flags.owndata == ownership


def test_manipulate_array_memory_empty_input():
    with pytest.raises(ValueError):
        manipulate_array_memory(np.array([]), True)


def test_manipulate_array_memory_invalid_input():
    with pytest.raises(TypeError):
        manipulate_array_memory(range(4), True)
