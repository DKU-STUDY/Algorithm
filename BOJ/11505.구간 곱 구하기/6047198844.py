import sys


def init(sgi, left, right):
    # 리프 노드인가
    if left == right:
        segment_tree[sgi] = arr[left]
    # 부모노드는 자식 노드의 곱이다.
    else:
        mid = (left + right) // 2
        segment_tree[sgi] = init(sgi * 2, left, mid) * init(sgi * 2 + 1, mid + 1, right) % 1000000007

    return segment_tree[sgi]


def update(sgi, left, right, i, new_value):
    # 범위를 벗어남
    if i < left or right < i:
        return

    # 리프노드
    if left == right:
        segment_tree[sgi] = new_value
        return

    # 현재 노드는 left ~ right 의 범위를 가진다.
    # 중간을 기준으로, i가 mid 보다 작거나 같으면 왼쪽 크면 오른쪽 자식이다.
    mid = (left + right) // 2
    update(2 * sgi, left, mid, i, new_value)
    update(2 * sgi + 1, mid + 1, right, i, new_value)
    segment_tree[sgi] = segment_tree[sgi*2] * segment_tree[sgi*2+1] % 1000000007


# 현재 sgi(세그먼트 인덱스) 의 범위는 left, right 이다. 우리는 begin, end 범위의 인덱스의 곱을 찾고 싶다.
def multiply(sgi, left, right, begin, end):
    # 현재 범위가 속하지 않는 범위라면?
    if left > end or right < begin:
        return 1
    # 현재 범위가 완전히 속해 있다면?
    if begin <= left and right <= end:
        return segment_tree[sgi]
    # 현재 범위가 걸쳐있다면?
    # 왼쪽 / 오른쪽 곱을 리턴한다.
    mid = (left + right) // 2
    return (multiply(2 * sgi, left, mid, begin, end) * multiply(2 * sgi + 1, mid + 1, right, begin, end)) % 1000000007


N, M, K = map(int, sys.stdin.readline().split())
segment_tree = [0 for _ in range(N * 4 + 1)]
arr = [0] + [int(sys.stdin.readline()) for _ in range(N)]

init(1, 1, N)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(1, 1, N, b, c)
    else:
        print(multiply(1, 1, N, b, c))
