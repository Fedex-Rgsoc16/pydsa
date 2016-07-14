# Longest Increasing Subsequence (LIS) using Dynamic Programming
# Complexity: O(n^2)

def longest_inc_subsequence(arr):

	"""
	Returns the length of the Longest Increasing Subsequence in an array using Dynamic Programming

	>>> from pydsa import longest_inc_subsequence
	>>> arr = [1, 12, 7, 0, 23, 11, 52, 31, 61, 69, 70, 2]
	>>> longest_inc_subsequence(arr)
	7
	"""

	size = len(arr)

	#Declaring an array which will contain the length of Longest increasing subsequence till ith index
	#Initialised all elements to 1, since length of Longest increasing subsequence till ith index would atleast be 1 
	lis_arr = [1]*size

	for i in range(0,size):
		for j in range(0,i):
			if arr[j]<arr[i] and lis_arr[i]<lis_arr[j]+1:
				lis_arr[i]=lis_arr[j]+1

	#Declaring and initialising max_lis_size to 0 to get the maximum of all lis_arr
	max_lis_size = 0

	for i in range(0,size):
		if max_lis_size < lis_arr[i]:
			max_lis_size = lis_arr[i]

	return max_lis_size