import pytest
from Functions.function1 import get_even_numbers


@pytest.mark.parametrize(["input_list", "expected_result"], [
    ([4, 6, 7, 8, 35, 34], [4, 6, 8, 34]),
    ([-4, 6, 7, 8], [-4, 6, 8]),
    ([], []),
    ([-4, 6, 7, 8, "a"], [-4, 6, 8]),
    ([-4, "#$%^&*()_", 6, 7, 8, "a"], [-4, 6, 8]),

])
def test_get_even_numbers(input_list, expected_result):
    result = get_even_numbers(input_list)
    assert result == expected_result
