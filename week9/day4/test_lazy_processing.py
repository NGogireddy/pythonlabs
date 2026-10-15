import pytest
from lazy_processing_streaming import lazy_version_squares, eager_version_squares


@pytest.mark.parametrize("orig_list, expected_result", [
    ([1, 2, 3, 'a'], [1, 4, 9]),
    ([1.0, 2.0], [1.0, 4.0]),
    ([], []),
])
def test_eager_version(orig_list, expected_result):
    result = eager_version_squares(orig_list)
    assert result == expected_result


@pytest.mark.parametrize("orig_list, expected_result", [
    ([1, 2, 3, 'a'], [1, 4, 9]),
    ([1.0, 2.0], [1.0, 4.0]),
    ([], []),
])
def test_lazy_version(orig_list, expected_result):
    gen = lazy_version_squares(orig_list)
    assert [square for square in gen] == expected_result

