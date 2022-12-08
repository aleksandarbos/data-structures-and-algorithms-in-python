"""
initial merge-sort implementation.
"""

def merge(A, B):
    """
    merges two ordered sequences of variable length. time complexity: O(len(A)+len(B))
    """
    count_a = 0
    count_b = 0

    if A == [] or B == []:
        raise Exception('Both A and B need to have at least one element.')

    while count_a < len(A) and count_b < len(B):
        if A[count_a] < B[count_b]:
            yield A[count_a]
            count_a += 1
        elif A[count_a] > B[count_b]:
            yield B[count_b]
            count_b += 1

    if count_a >= len(A):
        for i in range(count_b, len(B)):
            yield B[i]
    elif count_b >= len(B):
        for i in range(count_a, len(A)):
            yield A[i]

def merge_sort(seq):
    if len(seq) <= 2:
        if len(seq) == 2:
            if seq[0] > seq[1]:
                seq[0], seq[1] = seq[1], seq[0]
        return seq
    else:
        n = len(seq) // 2
        s1 = merge_sort(seq[:n])
        s2 = merge_sort(seq[n:])

        return list(merge(s1, s2))

if __name__ == "__main__":
    a = [85, 24, 63, 45, 17, 31, 96, 50, 100]
    assert merge_sort(a) == [17, 24, 31, 45, 50, 63, 85, 96, 100]
