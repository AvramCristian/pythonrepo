import pytest
from Functions.function1 import get_even_numbers

def test_get_even_numbers():
    list = [4,6,7,8]
    result = get_even_numbers(list)


    assert result == [4,6,8]

