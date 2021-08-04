'''
https://www.acmicpc.net/problem/1058
친구
[풀이]
1. 현재 상태가 친구인지 아닌지를 나타내는 friends 선언
2. 현재 2-친구인지 아닌지를 나타내는 board 선언
=> 처음에는 모든 원소가 초기값 0을 가진다.
3. friends 를 확인해 친구라면 1을 할당
=> 친구가 아니라면, 나와 친구인 친구가 그와도 친구인지 확인하고 친구라면 1을 할당
=> 친구가 아니라면 : board[y][x] == "N"
=> 나외 친구인 친구가 : board[y][z] == "Y"
=> 그와도 친구인지 : board[x][z] == "y"
4. 각 y축마다 2-친구 값을 모두 합친 값 중 최대를 출력
'''
n = int(input())
friends = [input() for _ in range(n)]
board = [[0] * n for _ in range(n)]
for y in range(n):
    for x in range(y+1, n):
        if friends[y][x] == "Y":
            board[y][x] = board[x][y] = 1
            continue
        for z in range(n):
            if friends[y][z] == friends[x][z] == "Y":
                board[y][x] = board[x][y] = 1
                break
print(max([sum(b) for b in board]))
