# 문제
# 성우가 정해놓은 방향은 총 4가지로 U, D, L, R이고 각각 위, 아래, 왼쪽, 오른쪽으로 이동하게 한다.
# 성우가 설정한 방향 지도가 주어졌을 때 재훈이를 도와서 영과일 회원들이 지도 어느 구역에 있더라도 성우가 피리를 불 때 ‘SAFE ZONE’에 들어갈 수 있게 하는 ‘SAFE ZONE’의 최소 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫 번째 줄에 지도의 행의 수를 나타내는 N(1 ≤ N ≤ 1,000)과 지도의 열의 수를 나타내는 M(1 ≤ M ≤ 1,000)이 주어진다.
#
# 두 번째 줄부터 N개의 줄에 지도의 정보를 나타내는 길이가 M인 문자열이 주어진다.
#
# 지도 밖으로 나가는 방향의 입력은 주어지지 않는다.
#
# 출력
# 첫 번째 줄에 ‘SAFE ZONE’의 최소 개수를 출력한다.
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
P = [i for i in range(N * M)]


def union(A, B):
    PA = find(A)
    PB = find(B)
    if PA == PB:
        return
    P[PB] = PA


def find(A):
    if A == P[A]:
        return A
    P[A] = find(P[A])
    return P[A]


for y in range(N):
    for x in range(M):
        i = (M * y) + x
        if board[y][x] == 'U':
            j = (M * (y - 1)) + x
        elif board[y][x] == 'D':
            j = (M * (y + 1)) + x
        elif board[y][x] == 'L':
            j = (M * y) + (x - 1)
        elif board[y][x] == 'R':
            j = (M * y) + (x + 1)
        union(i, j)

visited = set()
for y in range(N):
    for x in range(M):
        i = (M * y) + x
        Pi = find(i)
        if Pi not in visited:
            visited.add(Pi)
print(len(visited))