"""
세현이네 집에서 학교까지 가는 길은 N x N 크기의 바둑판과 같다.
그리고 각 블록은 1x1 정사각형으로 구분 지을 수 있다. 세현이는 그 블록마다 숫자와 연산자가 존재한다고 생각해서 임의의 숫자와 연산자를 각 블록에 넣어 바둑판을 만들었다.
세현이는 학교에서 집으로 가는 경로에서 만나는 숫자와 연산자의 연산 결과의 최댓값과 최솟값을 구하려고 한다.
세현이는 항상 자신의 집 (1, 1)에서 학교 (N, N)까지 최단거리로 이동한다. 최단거리로 이동하기 위해서는 오른쪽과 아래쪽으로만 이동해야 한다.
세현이는 이 길을 걸으면서 최댓값과 최솟값을 암산하다가 교통사고를 당해 현재 인하대학교 병원에 입원했다. 아픈 세현이를 위해 최댓값과 최솟값을 구해주자.
"""
N = int(input())
min_board = []
max_board = []
for _ in range(N):
    s = input()
    min_board.append(s.split())
    max_board.append(s.split())

#최소값 구하기.
for y in range(N):
    for x in range(N):
        i = j = 9999999
        k = l = -9999999
        if (y+x) % 2 == 0:
            # 좌
            if x-2 >= 0:
                i = eval(min_board[y][x-2] + min_board[y][x-1] + min_board[y][x])
                k = eval(max_board[y][x-2] + max_board[y][x-1] + max_board[y][x])
            # 상
            if y - 2 >= 0:
                j = eval(min_board[y - 2][x] + min_board[y - 1][x] + min_board[y][x])
                l = eval(max_board[y - 2][x] + max_board[y - 1][x] + max_board[y][x])

            if i != 9999999 or j != 9999999:
                min_board[y][x] = str(min(i,j))
                max_board[y][x] = str(max(k,l))


print(max_board[N-1][N-1], min_board[N-1][N-1])