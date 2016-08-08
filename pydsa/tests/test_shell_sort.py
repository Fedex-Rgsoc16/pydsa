from pydsa import shell_sort
from random import randint


def test_shell_sort():
    a = b = [randint(1, 100) for i in range(100)]
    assert shell_sort(a) == sorted(b)
