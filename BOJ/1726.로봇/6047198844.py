# 문제
# 우리 월드 공장의 로봇은 바라보는 방향으로 궤도를 따라 움직이며, 움직이는 방향은 동, 서, 남, 북 가운데 하나이다.
# 로봇의 이동을 제어하는 명령어는 다음과 같이 두 가지이다.
#
# 명령 1. Go k: k는 1, 2 또는 3일 수 있다. 현재 향하고 있는 방향으로 k칸 만큼 움직인다.
# 명령 2. Turn dir: dir은 left 또는 right 이며, 각각 왼쪽 또는 오른쪽으로 90° 회전한다.
#
# 공장 내 궤도가 설치되어 있는 상태가 아래와 같이 0과 1로 이루어진 직사각형 모양으로 로봇에게 입력된다.
#   0은 궤도가 깔려 있어 로봇이 갈 수 있는 지점
#   1은 궤도가 없어 로봇이 갈 수 없는 지점
#
# 로봇이 (4, 2) 지점에서 남쪽을 향하고 있을 때,  이 로봇을 (2, 4) 지점에서 동쪽으로 향하도록 이동시키는 것은 아래와 같이 9번의 명령으로 가능하다.
# 로봇의 현재 위치와 바라보는 방향이 주어졌을 때, 로봇을 원하는 위치로 이동시키고, 원하는 방향으로 바라보도록 하는데 최소 몇 번의 명령이 필요한지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 공장 내 궤도 설치 상태를 나타내는 직사각형의 세로 길이 M과 가로 길이 N이 빈칸을 사이에 두고 주어진다.
# 이때 M과 N은 둘 다 100이하의 자연수이다.
# 이어 M줄에 걸쳐 한 줄에 N개씩 각 지점의 궤도 설치 상태를 나타내는 숫자 0 또는 1이 빈칸을 사이에 두고 주어진다.
# 다음 줄에는 로봇의 출발 지점의 위치 (행과 열의 번호)와 바라보는 방향이 빈칸을 사이에 두고 주어진다.
# 마지막 줄에는 로봇의 도착 지점의 위치 (행과 열의 번호)와 바라보는 방향이 빈칸을 사이에 두고 주어진다.
# 방향은 동쪽이 1, 서쪽이 2, 남쪽이 3, 북쪽이 4로 주어진다. 출발지점에서 도착지점까지는 항상 이동이 가능하다.
#
# 출력
# 첫째 줄에 로봇을 도착 지점에 원하는 방향으로 이동시키는데 필요한 최소 명령 횟수를 출력한다.
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
start = tuple(map(lambda i: i - 1, map(int, sys.stdin.readline().split())))
end = tuple(map(lambda i: i - 1, map(int, sys.stdin.readline().split())))

# 동서남북 위치를 저장할 공간
visited = set()
Q = deque([start])
visited.add(start)

res = 0
if start == end:
    print(res)
    exit()

while Q:
    # 명령
    res += 1
    for _ in range(len(Q)):
        # 동 : 0 / 서 : 1 / 남 : 2 / 북 : 3
        y, x, direction = Q.popleft()
        # 0 -> 2,3 / 1 -> 2,3 / 2 -> 0,1 / 3 -> 0,1
        # 방향 전환
        commands = [(y, x, 2), (y, x, 3)] if direction == 0 or direction == 1 else [(y, x, 0), (y, x, 1)]

        # 이동
        if direction == 0:
            dy, dx = 0, 1
        elif direction == 1:
            dy, dx = 0, -1
        elif direction == 2:
            dy, dx = +1, 0
        else:
            dy, dx = -1, 0

        for ny, nx in (y + dy, x + dx), (y + (2 * dy), x + (2 * dx)), (y + (3 * dy), x + (3 * dx)):
            # 예외 처리: 이동할수있는 경우만 추가한다.
            if 0 <= ny < M and 0 <= nx < N and board[ny][nx] == 0:
                commands.append((ny, nx, direction))
            # 가다가 이동못하면 터트려야한다.
            else:
                break

        for my, mx, md in commands:
            # 기저 사례 : 끝난 경우
            if (my, mx, md) == end:
                print(res)
                exit()
            elif (my, mx, md) not in visited:
                visited.add((my, mx, md))
                Q.append((my, mx, md))