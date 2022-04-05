import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
segment_tree = [0] * (4 * N)


def init(sgi, begin, end):
    if begin == end:
        segment_tree[sgi] = arr[begin]
    else:
        mid = (begin + end) // 2
        segment_tree[sgi] = init(sgi * 2, begin, mid) + init(sgi * 2 + 1, mid + 1, end)
    return segment_tree[sgi]


# sgi 구간, 구하고자하는 구간
def sum(sgi, begin, end, left, right):
    if left > end or right < begin:
        return 0
    if left <= begin and end <= right:
        return segment_tree[sgi]
    mid = (begin + end) // 2
    return sum(sgi * 2, begin, mid, left, right) + sum(sgi * 2 + 1, mid + 1, end, left, right)


init(1, 1, N)
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sum(1, 1, N, i, j))
