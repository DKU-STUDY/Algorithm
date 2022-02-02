# 문제
# 출발은 상근이네 집에서 하고, 맥주 한 박스를 들고 출발한다.
# 맥주 한 박스에는 맥주가 20개 들어있다.
# 목이 마르면 안되기 때문에 50미터에 한 병씩 마시려고 한다. 즉, 50미터를 가려면 그 직전에 맥주 한 병을 마셔야 한다.
#
# 편의점에 들렸을 때, 빈 병은 버리고 새 맥주 병을 살 수 있다.
# 하지만, 박스에 들어있는 맥주는 20병을 넘을 수 없다.
# 편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 한다.
#
# 편의점, 상근이네 집, 펜타포트 락 페스티벌의 좌표가 주어진다.
# 상근이와 친구들이 행복하게 페스티벌에 도착할 수 있는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 t가 주어진다. (t ≤ 50)
# 각 테스트 케이스의 첫째 줄에는 맥주를 파는 편의점의 개수 n이 주어진다. (0 ≤ n ≤ 100).
# 다음 n+2개 줄에는 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표가 주어진다. 각 좌표는 두 정수 x와 y로 이루어져 있다. (두 값 모두 미터, -32768 ≤ x, y ≤ 32767)
# 송도는 직사각형 모양으로 생긴 도시이다. 두 좌표 사이의 거리는 x 좌표의 차이 + y 좌표의 차이 이다. (맨해튼 거리)
#
# 출력
# 각 테스트 케이스에 대해서 상근이와 친구들이 행복하게 페스티벌에 갈 수 있으면 "happy", 중간에 맥주가 바닥나서 더 이동할 수 없으면 "sad"를 출력한다.
import sys

t = int(input())


def is_connected(place1, place2):
    x1, y1 = place1
    x2, y2 = place2
    return (abs(x1 - x2) + abs(y1 - y2)) <= 1000


for _ in range(t):
    n = int(sys.stdin.readline())
    places = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n + 2)]
    # 연결되어있으면 True. 연결되있지않으면 False
    # 0번째 정점, n + 1 번째 정점이 True 인지 판단하면된다.
    # 초기화
    board = [[False for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n + 2):
        for j in range(i + 1, n + 2):
            board[i][j] = board[j][i] = is_connected(places[i], places[j])

    # 플로이드는 다이나믹 프로그래밍에 기반한다.
    # k 에 대해 전수조사하며 최적인지 검사한다.
    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                board[i][j] = board[i][j] or (board[i][k] and board[k][j])

    print("happy") if board[0][n + 1] else print("sad")
