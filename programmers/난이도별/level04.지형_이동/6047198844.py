import heapq
import collections


def solution(land, height):
    answer = 0
    N = len(land)
    area = [[-1 for i in range(N)] for j in range(N)]
    color = 0

    # 각 구간에 색깔을 칠해보자.
    for y in range(N):
        for x in range(N):
            if area[y][x] == -1:
                Q = [(y, x)]
                area[y][x] = color
                while Q:
                    yy, xx = Q.pop()
                    # bfs시작
                    for dy, dx in (-1, 0), (+1, 0), (0, -1), (0, +1):
                        ny = yy + dy
                        nx = xx + dx
                        if 0 <= ny < N and 0 <= nx < N and area[ny][nx] == -1 and abs(
                                land[yy][xx] - land[ny][nx]) <= height:
                            area[ny][nx] = color
                            Q.append((ny, nx))
                color += 1

    graph = [[0 for i in range(color)] for j in range(color)]
    # 구간에서 다른 구간을 이동할때 설치해야하는 사다리에 대해 계산한다. -> 색깔이 다르면 구간을 구한뒤 구간거리 갱신.
    for y in range(N):
        for x in range(N):
            for dy, dx in (-1, 0), (+1, 0), (0, -1), (0, +1):

                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    color1 = area[ny][nx]
                    color2 = area[y][x]

                    if color1 != color2:
                        dif = abs(land[y][x] - land[ny][nx])
                        if graph[color1][color2] == 0 or graph[color1][color2] > dif:
                            graph[color1][color2] = dif
                            graph[color2][color1] = dif

    spanning_tree = set()

    Q = [(0, 0)]
    # 해당 정보를 토대로 구간의 루트를 계산한다. -> 어떻게? 최소비용 간선트리.
    while Q and len(spanning_tree) != color:
        cost, cur_color = heapq.heappop(Q)
        if cur_color in spanning_tree:
            continue
        answer += cost
        spanning_tree.add(cur_color)
        for x in range(color):
            if graph[cur_color][x] != 0 and x not in spanning_tree:
                heapq.heappush(Q, (graph[cur_color][x], x))

    return answer

# 시간초과 . 추후 수정 필요.