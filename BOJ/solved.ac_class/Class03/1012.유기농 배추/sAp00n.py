from sys import stdin


def bfs(farm, i, j, M, N, visited):
    if farm[i][j] == 0:
        visited.append([i, j])
        return [0, visited]

    block = []
    queue = [[i, j]]

    while queue:
        [i, j] = queue.pop(0)
        block.append([i, j])
        visited.append([i, j])
        if farm[i][j] == 1:
            if i < N - 1 and farm[i + 1][j] == 1 and [i + 1, j] not in block and [i + 1, j] not in queue:
                queue.append([i + 1, j])
            if j < M - 1 and farm[i][j + 1] == 1 and [i, j + 1] not in block and [i, j + 1] not in queue:
                queue.append([i, j + 1])
            if j > 0 and farm[i][j - 1] == 1 and [i, j - 1] not in block and [i, j - 1] not in queue:
                queue.append([i, j - 1])
            if i > 0 and farm[i - 1][j] == 1 and [i - 1, j] not in block and [i - 1, j] not in queue:
                queue.append([i - 1, j])

    return [len(block), visited]


case = int(input())

for _ in range(case):
    M, N, K = map(int, stdin.readline().split())

    farm = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, stdin.readline().split())
        farm[Y][X] = 1

    visited = []
    result = 0

    for i in range(N):
        for j in range(M):
            if [i, j] not in visited:
                [size, visited] = bfs(farm, i, j, M, N, visited)
                if size != 0:
                    result += 1

    print(result)