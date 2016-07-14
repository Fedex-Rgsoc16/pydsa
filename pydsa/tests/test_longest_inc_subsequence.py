from pydsa.longest_inc_subsequence import longest_inc_subsequence

def test_longest_inc_subsequence():
	arr = [1, 12, 7, 0, 23, 11, 52, 31, 61, 69, 70, 2]
	result = longest_inc_subsequence(arr)
	assert result == 7