from pydsa.counting_inversions import counting_inversions


def test_counting_inversions():
    a = [1, 20, 6, 4, 5]
    b = counting_inversions(a)
    assert b == 5
