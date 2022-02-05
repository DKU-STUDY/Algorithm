# 문제
# 정사각형 모양을 한 다섯 종류의 색종이가 있다. 색종이의 크기는 1×1, 2×2, 3×3, 4×4, 5×5로 총 다섯 종류가 있으며, 각 종류의 색종이는 5개씩 가지고 있다.
#
# 색종이를 크기가 10×10인 종이 위에 붙이려고 한다.
# 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 0 또는 1이 적혀 있다. 1이 적힌 칸은 모두 색종이로 덮여져야 한다.
# 색종이를 붙일 때는 종이의 경계 밖으로 나가서는 안되고, 겹쳐도 안 된다. 또, 칸의 경계와 일치하게 붙여야 한다. 0이 적힌 칸에는 색종이가 있으면 안 된다.
#
# 종이가 주어졌을 때, 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수를 구해보자.
#
# 입력
# 총 10개의 줄에 종이의 각 칸에 적힌 수가 주어진다.
#
# 출력
# 모든 1을 덮는데 필요한 색종이의 최소 개수를 출력한다. 1을 모두 덮는 것이 불가능한 경우에는 -1을 출력한다.
import sys


# y, x 에 색종이를 붙였을때 색종이의 최소갯수로 교체한다.
def switch(y, x, K):
    for i in range(y, y + K + 1):
        for j in range(x, x + K + 1):
            board[i][j] = int(board[i][j] == 0)


def dfs(y, x, count):
    global ans
    # base case 1. y를 초과한경우.
    if y >= 10:
        ans = min(ans, count)
        return
    # base case 2. x를 초과한경우
    if x >= 10:
        dfs(y + 1, 0, count)
        return
    # bse case 3. board[y][x] 가 0 인 경우
    if board[y][x] == 0:
        dfs(y, x + 1, count)

    # 색종이를 붙여본다. 색종이는 각 종류마다 5개가 존재한다.
    # 색종이의 번호를 K라고 하자.
    for K in range(5):
        # 종이가 존재하는 지 확인한다.
        if paper[K] == 5:
            continue

        # 현재 위치에 색종이를 붙일 수 있다
        if y + K < 10 and x + K < 10:
            # 붙이는 지역이 모두 붙일수있는 지역인지 확인한다.
            flag = True
            for i in range(y, y + K + 1):
                for j in range(x, x + K + 1):
                    if board[i][j] == 0:
                        flag = False
                        break
                if not flag:
                    break

            # 뿥일수있다면
            if flag:
                # 붙인다.
                paper[K] += 1
                switch(y, x, K)
                # 다음 재귀를 호출한다.
                dfs(y, x + K + 1, count + 1)
                # 땐다.
                paper[K] -= 1
                switch(y, x, K)


board = [list(map(int, input().split())) for _ in range(10)]
paper = [0 for _ in range(5)]
ans = sys.maxsize
dfs(0, 0, 0)
print(-1) if ans == sys.maxsize else print(ans)
