import collections


#움직이고 싶은 marble의 위치, 움직이고 싶은 방향의 y, 움직이고 싶은 방향의 x
#가장 바깥 행과 열은 모두 막혀져 있다. (범위 체크하지 않아도 됨.)
#다 옮긴 후에는 옮겨진 marble의 위치, 움직인 길이를 반환한다.
#벽은 '#'으로 표현된다.
#원래 자리에서 움직일 위치가 '#'이면 안되고 원래 위치가 'O'이면 움직임을 멈춘다.
def move_marble(marble_position, dy, dx):
    y, x = marble_position
    moved_num = 0
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        moved_num += 1
        y += dy
        x += dx
    return y, x, moved_num

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
red_position = tuple()
blue_position = tuple()
for y in range(N):
    for x in range(M):
        if board[y][x] == 'R':
            red_position = (y, x)
        elif board[y][x] == 'B':
            blue_position = (y, x)

#bfs로 푼다.
#초기 포지션에 대해 큐에 넣는다
Q = collections.deque()
Q.append((red_position, blue_position))
path = set((red_position, blue_position))

#빨강구슬을 빼내는것이다. 파랑구슬을 빼면 실패이다.
cnt = 0
while Q:
    cnt += 1
    #현재의 움직임이 11번째일때 while문을 탈출한다.
    if cnt == 11:
        break

    for _ in range(len(Q)):
        red_position, blue_position = Q.popleft()

        #상하좌우로 움직인다.
        for dy, dx in (-1, 0), (+1, 0), (0, -1), (0, +1):
            n_red_y, n_red_x, n_moved_red = move_marble(red_position, dy, dx)
            n_blue_y, n_blue_x, n_moved_blue = move_marble(blue_position, dy, dx)
            #구멍은 두 구슬의 위치가 곂칠수있다.
            #움직인 위치가 blue를 구멍에 떨어뜨릴때. -> 더이상 진행하지 않는다.
            if board[n_blue_y][n_blue_x] == 'O':
                continue
            #움직인 위치가 red를 구멍에 떨어뜨릴때. -> 정답이다.
            elif board[n_red_y][n_red_x] == 'O':
                print(cnt)
                exit()
            #둘다 구멍에 위치하지 않는 경우. 위치가 곂치면 안된다.
            #곂칠경우 구슬에 대해서 바로 직전의 포지션으로 돌릴 필요가 있다.
            #길게 움직였다는것은 뒤에 있다는 뜻이다. 길게 움직인 marble의 위치를 한칸 무른다.
            #같은 길이는 움직일수없다. (동일한 위치에 있었다는 이야기이므로.)
            if n_red_y == n_blue_y and n_red_x == n_blue_x:
                if n_moved_red > n_moved_blue:
                    n_red_y += -dy
                    n_red_x += -dx
                else:
                    n_blue_y += -dy
                    n_blue_x += -dx

            n_marble_position = ((n_red_y, n_red_x), (n_blue_y, n_blue_x))
            #조정된 끝난 위치가 발견하지 않은 포지션인 경우 Q에 집어 넣는다.
            if n_marble_position not in path:
                #발견 완료
                path.add(n_marble_position)
                #Q에 넣는다.
                Q.append(n_marble_position)

#현재의 움직임이 11번째 & 공이 움직이지 않을때
print(-1)