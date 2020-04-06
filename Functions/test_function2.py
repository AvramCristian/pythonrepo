import pytest
from Functions.function2 import curata_lista


@pytest.mark.parametrize(["input_list", "expected_result"], [
    ([2, "erty", 20, "c", 5, 6], [2, 20, 5, 6]),
    ([5, 5, 56, "erty", 20, "c", 5, 6], [5, 5, 56, 20, 5, 6]),
    ([], []),
    (["sdfg", "sdtert", "@#$%^&"], []),
(   [2, 20,  5, 6], [2, 20, 5, 6])

])
def test_curata_lista(input_list, expected_result):
    result = curata_lista(input_list)
    assert result == expected_result
