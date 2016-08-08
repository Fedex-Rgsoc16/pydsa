# Shell Sort
# Complexity: O(n^2)


def shell_sort(a):
    """
    Sorts the list 'a' using Shell sort algorithm
    >>> from pydsa import bubble_sort
    >>> a = [3, 4, 2, 1, 12, 9]
    >>> bubble_sort(a)
    [1, 2, 3, 4, 9, 12]
    """
    length = len(a)
    i = int(length / 2)
    while (i > 0):
        for j in range(i, length):
            for k in range((j-i), -1, -i):
                if a[k+1] >= a[k]:
                    break
                else:
                    temp = a[k]
                    a[k] = a[k+i]
                    a[k+i] = temp
        i = int(i/2)
    return a
