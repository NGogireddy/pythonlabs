import pytest
import numpy as np
from unittest.mock import patch
from plotting_basics import plot_compounding_returns


@pytest.mark.parametrize('arr', [
    np.array([1, 2, 3]),
    np.empty((0, 2)),
    np.array([['1', '100']])
])
@patch('matplotlib.pyplot.show')
def test_invalid_scenarios(mock_show, arr):
    plot_compounding_returns(arr)
    mock_show.assert_not_called()


@patch('matplotlib.pyplot.show')
def test_valid_input(mock_show):
    arr = np.arange(6).reshape(2, 3)
    plot_compounding_returns(arr)
    mock_show.assert_called_once()
