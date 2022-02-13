# 문제
# 딸기우유 -> 초코우유 -> 바나나우유
# 이 도시는 정사각형 형태의 2차원 격자 모양으로  총 N*N개의 우유 가게들이 있다.
# 영학이는 도시의 서북쪽 끝 (1, 1)에서 출발해서 동남쪽 아래 (N, N)까지 까지 가면서 우유를 사 마신다.
# 각각의 우유 가게는 딸기, 초코, 바나나 중 한 종류의 우유만을 취급한다.
# 각각의 우유 가게 앞에서, 영학이는 우유를 사 마시거나, 사 마시지 않는다.
# 영학이는 오직 동쪽 또는 남쪽으로만 움직이기 때문에 한 번 지나친 우유 가게에는 다시 가지 않는다.
# 영학이가 마실 수 있는 우유의 최대 개수를 구하여라.
#
# 입력
# 첫 번째 줄에는 우유 도시의 영역 크기 N이 주어진다. (1 ≤ N ≤ 1000)
# 두 번째 줄부터 N+1 번째 줄까지 우유 도시의 정보가 주어진다.
# 0은 딸기우유만을 파는 가게, 1은 초코우유만을 파는 가게, 2는 바나나우유만을 파는 가게를 뜻하며, 0, 1, 2 외의 정수는 주어지지 않는다.
#
# 출력
# 영학이가 마실 수 있는 우유의 최대 개수를 출력하시오.
import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 딸기우유 / 초코우유 / 바나나우유 를 마지막으로 먹었을때 먹은 우유의 수를 메모한다.
memo = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]

# base case 1 : 딸기우유를 마신다
if board[0][0] == 0:
    memo[0][0][0] = 1

for y in range(N):
    for x in range(N):
        # 북쪽에서 온 경우 / 서쪽에서 온경우
        for dy, dx in (0, -1), (-1, 0):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                for i in range(3):
                    memo[y][x][i] = max(memo[y][x][i], memo[ny][nx][i])

                # 현재 상점의 우유 종류
                cur_milk_type = board[y][x]
                # 이전 우유 종류
                pre_milk_type = (cur_milk_type - 1) % 3

                # 이전에 우유를 마신 상태여야한다.
                if memo[y][x][pre_milk_type] != 0:
                    memo[y][x][cur_milk_type] = max(memo[ny][nx][pre_milk_type] + 1, memo[y][x][cur_milk_type])
                # 이전에 안마셨다면 지금 마신다.
                elif cur_milk_type == 0:
                    memo[y][x][cur_milk_type] = 1

print(max(memo[N-1][N-1]))