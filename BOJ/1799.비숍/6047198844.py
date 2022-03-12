# 문제
# 서양 장기인 체스에는 대각선 방향으로 움직일 수 있는 비숍(bishop)이 있다.
# 비숍은 대각선 방향으로 움직여 다른 말을 잡을 수 있다.
#
# 그런데 체스판 위에는 비숍이 놓일 수 없는 곳이 있다.
# 색칠된 부분에는 비숍이 놓일 수 없지만 지나갈 수는 있다.
#
# 정사각형 체스판의 한 변에 놓인 칸의 개수를 체스판의 크기라고 한다. 체스판의 크기와 체스판 각 칸에 비숍을 놓을 수 있는지 없는지에 대한 정보가 주어질 때, 서로가 서로를 잡을 수 없는 위치에 놓을 수 있는 비숍의 최대 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 체스판의 크기가 주어진다. 체스판의 크기는 10이하의 자연수이다.
# 둘째 줄부터 아래의 예와 같이 체스판의 각 칸에 비숍을 놓을 수 있는지 없는지에 대한 정보가 체스판 한 줄 단위로 한 줄씩 주어진다. 비숍을 놓을 수 있는 곳에는 1, 비숍을 놓을 수 없는 곳에는 0이 빈칸을 사이에 두고 주어진다.
#
# 출력
# 첫째 줄에 주어진 체스판 위에 놓을 수 있는 비숍의 최대 개수를 출력한다.
import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

left_visited = [False for _ in range(2 * N - 1)]
right_visited = [False for _ in range(2 * N - 1)]


# y, x에 비숍을 위치하거나 위치하지 않았을때 놓을수있는 비숍의 최대 개수
def backtracking(y, x):
    # base case : 종료 조건
    if y == N:
        return 0

    # 예외 : x 범위를 벗어남
    if x >= N:
        return backtracking(y + 1, (x + 1) % 2)

    # 현재 위치에 비숍을 놓지 않는 경우
    res = backtracking(y, x + 2)

    # 현재 위치에 비숍을 놓는 경우
    if board[y][x] == 1 and left_visited[y + x] == False and right_visited[N - 1 + y - x] == False:
        left_visited[y + x] = right_visited[N - 1 + y - x] = True
        res = max(res, 1 + backtracking(y, x + 2))
        left_visited[y + x] = right_visited[N - 1 + y - x] = False

    return res


print(backtracking(0, 0) + backtracking(0, 1))
