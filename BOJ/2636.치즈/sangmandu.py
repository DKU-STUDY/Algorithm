'''
https://www.acmicpc.net/problem/2636
치즈
[풀이]
1. main
1-1. 사전 세팅
=> 재귀제한을 2000으로 늘려줘야 한다
=> 반복적인 입력이 최대 만번이므로 sys.stdin.readline을 사용
=> 가로와 세로를 저장할 w, h 그리고 모양을 저장할 board를 선언
=> 탐색을 위한 move, 녹아 없어지는 시간 time, 치즈 개수 prev_cheese를 선언
1-2. 공기 구별
=> 2. check_air 에서 확인한다
=> 치즈 바깥쪽에 있는 공기와 안쪽에 있는 공기를 구별해야 한다
=> 바깥쪽에 있는 공기는 -1로 바꿔주도록 한다
확인 조건은, 주변 원소가 -1 이거나 벽과 닿아있으면.
=> 중요한 점은, 탐색이 모두 끝난후에 바꿔야 한다는 점.
따라서, set을 사용해서 중복을 제거하며 미리 넣어두고 탐색이 끝난 후 하나씩 꺼내면서 치환
1-3. 출력 조건
=> 공기를 구별하기 위해 조건을 확인하면서 치즈 개수도 센다
=> 치환 후에 치즈 개수가 0이면, 모든 치즈가 녹기 한 시간전의 치즈 개수 prev_cheese를 반환
1-4. 녹는 조건
=> check_melt() 함수로 확인
=> 자신을 기준, 상하좌우로 -1을 가진 공기가 있다면 자신은 녹는다.
2. check_air
2-1. flag = 0으로 선언.
=> 인자로 받은 좌표가 바깥쪽에 있는 공기로 판단되면 flag가 1 이상의 값을 가진다
2-2. 바깥쪽에 있는 공기 판단 조건
=> 벽에 닿아있거나, 주변 공기가 -1
2-3. 만약, 자신이 0인 공기면서 outer_air에 포함되어있지 않으면 자신을 중심으로 다시 check_air
=> 이 때 outer_air는 set() 자료형으로 방문여부를 확인하는 기능
=> 또, 아직은 0인 공기지만 추후에 -1인 공기로 밝혀진다면 이 때 모든 air를 치환할 수 있도록
방문했던 공기를 기억해주는 역할.

'''
def check_air(board, y, x):
    flag = 0
    for dy, dx in move:
        ny, nx = dy+y, dx+x
        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            flag += 1
            continue
        if board[ny][nx] == -1:
            flag += 1
            continue
        if board[ny][nx] == 0 and (ny, nx) not in outer_air:
            outer_air.add((ny, nx))
            flag += check_air(board, ny, nx)
    return flag

def check_melt(y, x):
    for dy, dx in move:
        ny, nx = dy + y, dx + x
        if board[ny][nx] == -1:
            return True
    return False

import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline
h, w = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(h)]
move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
time = 0
prev_cheese = 0
while True:
    total_cheese = 0
    for y in range(h):
        for x in range(w):
            outer_air = set()
            if board[y][x] == 0 and (y, x) not in outer_air:
                outer_air.add((y, x))
                flag = check_air(board, y, x)
                if flag > 0:
                    for ny, nx in list(outer_air):
                        board[ny][nx] = -1
            elif board[y][x] == 1:
                total_cheese += 1

    if total_cheese == 0:
        print(time)
        print(prev_cheese)
        break

    melt = set()
    for y in range(h):
        for x in range(w):
            if board[y][x] == 1:
                if check_melt(y, x):
                    melt.add((y, x))
    for ny, nx in list(melt):
        board[ny][nx] = -1

    time += 1
    prev_cheese = total_cheese
