# 문제

# 그가 만든 모래성을 2차원 격자단위로 만들었으며, 각 격자마다 튼튼함의 정도를 다르게 해서 성을 만들었다.
#   1부터 9 사이의 숫자로 표현될 수 있다.
#   자기 격자 주변의 8방향 (위 아래 왼쪽 오른쪽, 그리고 대각선) 을 봐서 모래성이 쌓여있지 않은 부분의 개수가 자기 모래성의 튼튼함보다 많거나 같은 경우 파도에 의해서 무너질 수 있음을 의미한다.
#   그 이외의 경우는 파도가 쳐도 무너지지 않는다. 모래성이 무너진 경우, 그 격자는 모래성이 쌓여있지 않은 것으로 취급한다.
#
# 이 모래성은 언젠가는 파도에 의해서 깎이고 깎여서, 결국 한가지 형태로 수렴할 것이다. 모래성을 완성한 명우는 문득 자신이 만든 예술품의 수명이 궁금해졌다.
# 모래성은 위에 서술한 바와 같이 파도가 한번 칠 때마다 특정 부분이 무너저내리는 방식으로 모양이 변화된다. 모래성이 더이상 모양이 변하지 않게 되려면 (모양이 수렴되려면) 파도가 몇번 쳐야하는지 구해보자.
#
# 입력
# 첫째 줄에는 모래성의 가로세로 격자 크기 H, W가 주어진다. (1 ≤ H, W ≤ 1,000)
#
# 그 다음 H줄에 걸쳐 W개의 문자로 모래성의 상태를 나타내는 문자가 들어온다.
#
# 각 문자는 1~9 사이의 숫자, 또는 '.' 이다. 1~9는 그 격자의 모래의 강도를 나타내며, '.'는 모래가 없다는 뜻이다.
#
# 모래성은 격자의 가장자리와 접해 있지 않다.
#
# 출력
# 몇번의 파도가 몰려오고나서야 모래성의 상태가 수렴하는지를 구한다.
import sys
from collections import deque

H, W = map(int, sys.stdin.readline().split())
# 전처리
board = [list(map(int, sys.stdin.readline().rstrip().replace('.', '0'))) for _ in range(H)]

# 파도에 의해 무너질 가능성이 있는 구역
Q = deque([])
for y in range(1, H - 1):
    for x in range(1, W - 1):
        # 0 , 9 는 가능성이 없다.
        if board[y][x] != 0 and board[y][x] != 9:
            Q.append((y, x))

res = 0
while Q:
    # 파도에 의해 무너진 구역
    # 0으로 확인할수있으나 구현과정에서 저장할곳이 필요함. 즉 임시저장소임.
    broken_Q = deque([])

    # 파도에 의해 무너질 가능성이 있는 구역
    next_Q = deque([])
    next_visited = set()

    # 파도가 친다.
    res += 1
    while Q:
        y, x = Q.popleft()

        # 이미 무너졌는지 확인
        # 파도에 의해 없어졌을 가능성이 존재한다.
        if board[y][x] == 0:
            continue

        cnt = 0
        # 내구성 테스트
        for ny, nx in (y - 1, x), (y - 1, x - 1), (y, x - 1), (y + 1, x - 1), (y + 1, x), (y + 1, x + 1), (y, x + 1), (y - 1, x + 1):
            cnt += int(board[ny][nx] == 0)

        # 무너진 경우
        if cnt >= board[y][x]:
            # 이번 파도에 의해 무너진 구역에 추가한다.
            broken_Q.append((y, x))
            board[y][x] = -1

            # 주변을 다음 큐에 넣는다.
            # 파도에 의해 무너질 가능성이 있는 구역에 추가한다.
            for ny, nx in (y - 1, x), (y - 1, x - 1), (y, x - 1), (y + 1, x - 1), (y + 1, x), (y + 1, x + 1), (y, x + 1), (y - 1, x + 1):
                # 이미 추가된 구역 / 무너진 구역이 아니여야한다. 또한 0과 9는 무너질 가능성이 없으므로 넣지 않는다.
                if (ny, nx) not in next_visited and board[ny][nx] != -1 and board[ny][nx] != 0 and board[ny][nx] != 9:
                    next_Q.append((ny, nx))
                    next_visited.add((ny, nx))

    # 무너진 구역이 없는 경우. 이전 파도는 영향을 끼치지 못했으므로 수렴했다는 뜻이다. 1을 감소시키고 종료한다.
    if len(broken_Q) == 0:
        res -= 1
        break

    # 무너진다.
    while broken_Q:
        y, x = broken_Q.popleft()
        board[y][x] = 0

    # 다음 방문으로 교체한다.
    Q = next_Q


print(res)