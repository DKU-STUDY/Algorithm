
n= int(input())
k= int(input())
apple=[list(map(int, input().split())) for _ in range(k)] # (1, 1)에는 사과가 없음
l= int(input())
dir_change= [input().split() for _ in range(l)]
snake= [[0, 0]]
dir= 'R'
board=[[0]*n for _ in range(n)]
directions= ['R', 'L', 'U', 'D']
d= [[0, 1], [0, -1], [-1, 0], [1, 0]]
cnt= 0
x, y= 0, 0

for a, b in apple:
    board[a-1][b-1]= 2

while True:
    cnt+=1

    # 방향 전환 후 전진
    for i in range(len(directions)):
        if dir == directions[i]:
            tx, ty = x + d[i][0], y + d[i][1]

    if 0 <= tx < n and 0 <= ty < n and board[tx][ty] != 1:
        if board[tx][ty]==2:
            # print([tx, ty], "apple")
            snake.append([tx, ty]);
            board[tx][ty] = 1
            apple.pop(0)
        else:
            px, py = snake.pop(0)
            snake.append([tx, ty])
            board[tx][ty] = 1
            board[px][py] = 0

    else:
        break;

    x, y = tx, ty
    # print(snake)
    # print(cnt, dir)
    # for i in board:
    #     print(i)
    # print()

    # 방향 전환
    if dir_change != [] and cnt== int(dir_change[0][0]):
        if dir=='R':
            if dir_change[0][1]== 'L': dir='U'
            else: dir='D'
        elif dir=='L':
            if dir_change[0][1]== 'L': dir='D'
            else: dir='U'
        elif dir=='U':
            if dir_change[0][1]=='L': dir='L'
            else: dir= 'R'
        elif dir=='D':
            if dir_change[0][1]=='L': dir='R'
            else: dir= 'L'
        dir_change.pop(0)

print(cnt)




