from Sesiunea8.Testing_example.App.Func import is_div_3_5
import pytest


def test_is_div_3_5_example():
    assert is_div_3_5(25) == 5


@pytest.mark.parametrize("n, expected", [
    (15, 35),
    (9, 3),
    (10, 5),
    (4, None)
])
def test_is_div_3_5(n, expected):
    assert is_div_3_5(n) == expected

