# Counting Inversions Using Merge Sort
# Complexity: O(nlog(n))

# get_divide function divides the array into left and right halves


def get_divide(a):
    size = len(a)
    Left = []
    Right = []
    mid_size = int(size/2)
    for index in range(0, mid_size):
        Left.append(a[index])

    for index in range(mid_size, size):
        Right.append(a[index])

    return [Left, Right]

# count function merges the two sorted arrays and count the number of
# inversions


def count(Left, Right):
    new_arr, i, j = [], 0, 0
    inv_count = 0
    size_left = len(Left)
    size_right = len(Right)

    while i < size_left and j < size_right:
        if Left[i] <= Right[j]:
            new_arr.append(Left[i])
            i += 1
        else:
            new_arr.append(Right[j])
            j += 1
            inv_count += (size_left - i)
    # When a[i] > a[j], all elements remaining in left array are greater
    # than a[j], hence num_inversions = inv_count + size_left_array - 1

    if i == size_left:
        new_arr.extend(Right[j:])
    else:
        new_arr.extend(Left[i:])
    return new_arr, inv_count

# merge_sort function takes input of an array and recursively
# applies merge sort to it


def merge_sort(a):
    size_arr = len(a)
    if size_arr >= 2:
        [Left, Right] = get_divide(a)
        Left, lInv = merge_sort(Left)
        Right, rInv = merge_sort(Right)
        Mid, mInv = count(Left, Right)
        return Mid, (lInv + rInv + mInv)
    else:
        return a, 0


# counting_inversions function returns the number of inversions

def counting_inversions(a):
    """
    Counts the Inversions in the list 'a' using Merge Sort algorithm

    >>> from pydsa import counting_inversions
    >>> a = [1, 20, 6, 4, 5]
    >>> counting_inversions(a)
    5

    """
    arr, num_inversions = merge_sort(a)
    return num_inversions
