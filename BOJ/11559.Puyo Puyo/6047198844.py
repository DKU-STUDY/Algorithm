# 문제
# 뿌요뿌요의 룰은 다음과 같다.
# 필드에 여러 가지 색깔의 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다.
# 뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.
# 뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.
# 아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.
# 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.
# 이 게임은 1:1로 붙는 대전게임이라 잘 쌓는 것도 중요하지만, 상대방이 터뜨린다면 연쇄가 몇 번이 될지 바로 파악할 수 있는 능력도 필요하다.
# 상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산하여 남규를 도와주자!
#
# 입력
# 총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.
# 이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.
# R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.
#
# 입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태이다. 즉, 뿌요 아래에 빈 칸이 있는 경우는 없다.
#
# 출력
# 현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 터지지 않는다면 0을 출력한다.
from collections import deque

board = [list(input()) for _ in range(12)]
res = 0

while True:
    # 연속이 있는지 검사.
    visited = set()
    # 연쇄가 있어서 pop 했는지 여부
    is_pop = False

    for iy in range(12):
        for ix in range(6):
            if board[iy][ix] != '.' and (iy, ix) not in visited:
                group = list()
                Q = deque()

                group.append((iy, ix))
                Q.append((iy, ix))
                visited.add((iy, ix))

                # iy, ix 와 연결되어있는 색깔을 모두 찾는다.
                while Q:
                    y, x = Q.popleft()
                    for dy, dx in (-1, 0), (+1, 0), (0, -1), (0, +1):
                        ny = y + dy
                        nx = x + dx
                        if 0 <= ny < 12 and 0 <= nx < 6 and (ny, nx) not in visited and board[ny][nx] == board[iy][ix]:
                            group.append((ny, nx))
                            Q.append((ny, nx))
                            visited.add((ny, nx))
                # 연결된 뿌요의 숫자가 4개 이상이면 터트린다. (점으로 만든다.)
                # 터트렸으므로 flag 값을 True 로 한다.
                if len(group) >= 4:
                    while group:
                        pop_y, pop_x = group.pop()
                        board[pop_y][pop_x] = '.'
                    is_pop = True
    if not is_pop:
        break

    # 내린다.
    for x, column in enumerate(zip(*board)):
        new_column = list(filter(lambda i: i != '.', column))[::-1]
        if new_column:
            for y in range(len(new_column)):
                board[11 - y][x] = new_column[y]
            for y in range(len(new_column), len(column)):
                board[11 - y][x] = '.'
    res += 1

print(res)