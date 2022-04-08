# 문제
# 각각의 사탕은 그 맛의 좋고 나쁨이 1부터 1,000,000까지의 정수로 구분된다.
# 1이 가장 맛있는 사탕을 의미하며, 1,000,000은 가장 맛없는 사탕을 의미한다.
# 수정이는 동생이 말을 잘 들은 정도에 따라서, 사탕상자 안에 있는 사탕들 중 몇 번째로 맛있는 사탕을 꺼내주곤 한다.
# 예를 들어 말을 매우 잘 들었을 때에는 사탕상자에서 가장 맛있는 사탕을 꺼내주고, 말을 조금 잘 들었을 때에는 사탕상자에서 여섯 번째로 맛있는 사탕을 꺼내주는 식이다.
#
# 수정이가 보관하고 있는 사탕은 매우 많기 때문에 매번 사탕상자를 뒤져서 꺼낼 사탕을 골라내는 일은 매우 어렵다. 수정이를 도와주는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수정이가 사탕상자에 손을 댄 횟수 n(1 ≤ n ≤ 100,000)이 주어진다.
# 다음 n개의 줄에는 두 정수 A, B, 혹은 세 정수 A, B, C가 주어진다. A가 1인 경우는 사탕상자에서 사탕을 꺼내는 경우이다. 이때에는 한 정수만 주어지며, B는 꺼낼 사탕의 순위를 의미한다.
# 이 경우 사탕상자에서 한 개의 사탕이 꺼내지게 된다. 또, A가 2인 경우는 사탕을 넣는 경우이다. 이때에는 두 정수가 주어지는데, B는 넣을 사탕의 맛을 나타내는 정수이고 C는 그러한 사탕의 개수이다.
# C가 양수일 경우에는 사탕을 넣는 경우이고, 음수일 경우에는 빼는 경우이다. 맨 처음에는 빈 사탕상자에서 시작한다고 가정하며, 사탕의 총 개수는 2,000,000,000을 넘지 않는다. 또한 없는 사탕을 꺼내는 경우와 같은 잘못된 입력은 주어지지 않는다.
#
# 출력
# A가 1인 모든 입력에 대해서, 꺼낼 사탕의 맛의 번호를 출력한다.
import sys

MAX = 1000000
tree = [0] * (4 * MAX)


def update(sgi, begin, end, i, diff):
    tree[sgi] += diff
    if begin == end:
        return

    mid = (begin + end) // 2
    if i <= mid:
        update(sgi * 2, begin, mid, i, diff)
    else:
        update(sgi * 2 + 1, mid + 1, end, i, diff)


def sum(sgi, begin, end, left, right):
    if end < left or right < begin:
        return 0
    if left <= begin and end <= right:
        return tree[sgi]

    mid = (begin + end) // 2
    return sum(sgi * 2, begin, mid, left, right) + sum(sgi * 2 + 1, mid + 1, right, left, right)


n = int(sys.stdin.readline())
for _ in range(n):
    cmd = list(map(int, sys.stdin.readline().split()))
    if len(cmd) == 2:
        # 순위
        B = cmd[1]
        # 순위를 어떻게 구해야하나?
        # 이분 탐색해보자
        begin, end, sgi = 1, MAX, 1

        while begin < end:
            mid = (begin + end) // 2
            left, right = tree[sgi*2], tree[sgi*2 + 1]

            # 왼쪽을 택하는 경우.
            if B <= left:
                # 순위는 그대로
                # 범위는 좁아진다.
                end = mid
                sgi *= 2
            # 오른쪽을 택하는 경우.
            else:
                # 순위는 낮아진다.
                B -= tree[sgi*2]
                begin = mid + 1
                sgi = sgi * 2 + 1
        print(begin)
        update(1, 1, MAX, begin, -1)

    else:
        update(1, 1, MAX, cmd[1], cmd[2])
