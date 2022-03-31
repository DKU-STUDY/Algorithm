import sys

sys.setrecursionlimit(10 ** 9)


def distance(ay, ax, by, bx):
    return abs(ay - by) + abs(ax - bx)


N = int(sys.stdin.readline())
W = int(sys.stdin.readline())
# arr[idx] 경찰차가 idx를 택했을때의 위치
arr = [(0, 0)] + [tuple(map(int, sys.stdin.readline().split())) for _ in range(W)]
# memo[A][B] 0번 경찰차가 A, 1번 경찰차가 B를 택했을때 이동하는 거리의 합
memo = [[-1 for _ in range(W + 1)] for _ in range(W + 1)]
path = [[-1 for _ in range(W + 1)] for _ in range(W + 1)]


# A와 B는 각각 0번/1번 경찰차가 어디 idx 에 있는지 나타낸다.
# func(A,B)는 0번/1번 경찰차가 arr[A], arr[B] 위치에 있을때, 두대의 경찰차가 이동하는 거리의 최소 합이다.
# 핵심 아이디어는 A,B 중 가장 큰수가 갱신된 수라는 점이다.
def func1(A, B):
    # base case: 범위 체크
    if A == W or B == W:
        return 0

    # base case2: 메모 되었는가
    if memo[A][B] != -1:
        return memo[A][B]

    # 다음 스텝 -> 가장 최근것에 1 더한다.
    next = max(A, B) + 1

    # A를 이동 시킨다.
    # 이전거리 -> 이동거리
    if A == 0:
        move_a = distance(1, 1, arr[next][0], arr[next][1])
    else:
        move_a = distance(arr[A][0], arr[A][1], arr[next][0], arr[next][1])

    # B를 이동 시킨다.
    if B == 0:
        move_b = distance(N, N, arr[next][0], arr[next][1])
    else:
        move_b = distance(arr[B][0], arr[B][1], arr[next][0], arr[next][1])

    a_result = func1(next, B) + move_a
    b_result = func1(A, next) + move_b

    memo[A][B] = min(a_result, b_result)
    return memo[A][B]


# 루트를 구하는 함수. 이미 메모는 완성되어있는상태 (func1이 반드시 선행된다.).
def func2(A, B):
    if A == W or B == W:
        return

    next = max(A, B) + 1

    # A를 이동 시킨다.
    # 이전거리 -> 이동거리
    if A == 0:
       move_a = distance(1, 1, arr[next][0], arr[next][1])
    else:
        move_a = distance(arr[A][0], arr[A][1], arr[next][0], arr[next][1])

    # B를 이동 시킨다.
    if B == 0:
        move_b = distance(N, N, arr[next][0], arr[next][1])
    else:
        move_b = distance(arr[B][0], arr[B][1], arr[next][0], arr[next][1])

    # 재귀 타지 않고 어떤게 최선인지 바로 구할수있음.
    # A를 택하는게 최선인 경우
    if memo[next][B] + move_a < memo[A][next] + move_b:
        print(1)
        func2(next, B)
    else:
        print(2)
        func2(A, next)


func1(0, 0)
print(memo[0][0])
func2(0, 0)