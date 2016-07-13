# Counting Inversions Using Merge Sort
# Complexity: O(nlog(n))

def get_divide(a):
    s = len(a)
    L=[]
    R=[]
    for i in xrange(0,s/2):
        L.append(a[i])

    for i in xrange(s/2,s):
        R.append(a[i])

    return [L,R]


def count(L, R):
    m, i, j = [], 0, 0
    icount = 0
    l1 = len(L)
    l2 = len(R)
    while i < l1 and j < l2:
        if L[i] <= R[j]:
            m.append(L[i])
            i += 1
        else:
            m.append(R[j])
            j += 1
            icount += (l1-i)
    if i == l1:
        m.extend(R[j:])
    else:
        m.extend(L[i:])
    return m, icount


def merge_sort(a):
    l = len(a)
    if l >= 2:
        [L,R] = get_divide(a)
        L,lInv = merge_sort(L)
        R,rInv = merge_sort(R)
        M,mInv = count(L,R)
        return M,(lInv + rInv + mInv)
    else:
        return a, 0


def counting_inversions(a):
    """
    Counts the Inversions in the list 'a' using Merge Sort algorithm

    >>> from pydsa import counting_inversions
    >>> a = [1, 20, 6, 4, 5]
    >>> counting_inversions(a)
    5

    """
    p,q = merge_sort(a)
    return q