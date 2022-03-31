# 문제
# N(1 ≤ N ≤ 100,000)개의 정수들이 있을 때, a번째 정수부터 b번째 정수까지 중에서 제일 작은 정수, 또는 제일 큰 정수를 찾는 것은 어려운 일이 아니다. 하지만 이와 같은 a, b의 쌍이 M(1 ≤ M ≤ 100,000)개 주어졌을 때는 어려운 문제가 된다. 이 문제를 해결해 보자.
#
# 여기서 a번째라는 것은 입력되는 순서로 a번째라는 이야기이다. 예를 들어 a=1, b=3이라면 입력된 순서대로 1번, 2번, 3번 정수 중에서 최소, 최댓값을 찾아야 한다. 각각의 정수들은 1이상 1,000,000,000이하의 값을 갖는다.
#
# 입력
# 첫째 줄에 N, M이 주어진다. 다음 N개의 줄에는 N개의 정수가 주어진다. 다음 M개의 줄에는 a, b의 쌍이 주어진다.
#
# 출력
# M개의 줄에 입력받은 순서대로 각 a, b에 대한 답을 최솟값, 최댓값 순서로 출력한다.

# sgi 를 초기화한다. sgi의 구간은 left, right 이다.
import math
import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0] + [int(sys.stdin.readline()) for _ in range(N)]
# 최소값 / 최대값
segment_tree = [(math.inf, -math.inf)] * (N * 4)


def init(sgi, left, right):
    # 리프노드에 도달
    if left == right:
        segment_tree[sgi] = (min(arr[left:right + 1]), max(arr[left:right + 1]))
    else:
        mid = (left + right) // 2
        min_left_child, max_left_child = init(sgi * 2, left, mid)
        min_right_child, max_right_child = init(sgi * 2 + 1, mid + 1, right)
        segment_tree[sgi] = (min(min_left_child, min_right_child), max(max_left_child, max_right_child))

    return segment_tree[sgi]


init(1, 1, N)

# 현재 sgi 구간 left ~ right
# 찾고자하는 구간 begin ~ end
def find(sgi, left, right, begin, end):
    # 현재 구간이 찾고자하는 구간이 아닌 경우
    if end < left or right < begin:
        return math.inf, -math.inf

    # 현재 구간이 안에 들어와 있는 경우
    if begin <= left and right <= end:
        return segment_tree[sgi]

    # 현재 구간이 걸친 경우
    mid = (left + right) // 2
    min_left_child, max_left_child = find(sgi * 2, left, mid, begin, end)
    min_right_child, max_right_child = find(sgi * 2 + 1, mid + 1, right, begin, end)

    return min(min_left_child, min_right_child), max(max_left_child, max_right_child)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    min_value, max_value = find(1, 1, N, a, b)
    print(min_value, max_value)