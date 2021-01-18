'''
https://www.acmicpc.net/problem/14502
14502 연구소
BFS 이용 : 기둥을 3개씩 세우는 모든 경우의 수를 계산한다
N, M이 8보다 작기 때문에 이게 돌아갈까? 하는 걱정을 좀 덜어도 된다.
'''

from itertools import combinations

def dfs(y, x):
    for ay, ax in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny, nx = y + ay, x + ax
        if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and adj[ny][nx] == 0:
            visited[ny][nx] = 1
            dfs(ny, nx)
    return

n, m = map(int, input().split())
adj = []
for i in range(n):
    adj.append(list(map(int, input().split())))

col_list = []
index = [(y, x) for y in range(n) for x in range(m)]
for case in combinations(index, 3):
    col = [(y, x) for y, x in case if adj[y][x] == 0]
    if len(col) == 3:
        col_list.append(col)

ret = []
virus_list = [(y, x) for y in range(n) for x in range(m) if adj[y][x] == 2]
column_num = sum([row.count(1) for row in adj]) + 3
for col in col_list:
    for y, x in col:
        adj[y][x] = 1
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for y, x in virus_list:
        visited[y][x] = 1
        dfs(y, x)
    ret.append(sum([row.count(0) for row in visited])-column_num)

    for y, x in col:
        adj[y][x] = 0

print(max(ret))

'''
항상 풀이할 때 수학적인 부분으로 해결이 가능한지 고민하다 보니 시간이 걸린 문제
N, M 이 8 이하인 것 보고 컴퓨터 식으로 일일이 해결해야 된다고 생각
'''