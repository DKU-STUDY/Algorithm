import heapq
import collections

parent = list()


def find(color):
    if color == parent[color]:
        return color
    else:
        p = find(parent[color])
        parent[color] = p
        return p


def union(color1, color2):
    color1 = find(color1)
    color2 = find(color2)
    if color1 != color2:
        parent[color2] = color1
        return True
    return False


def solution(land, height):
    answer = 0
    N = len(land)
    area = [[-1 for i in range(N)] for j in range(N)]
    graph = set()
    color = 0

    # 각 구간에 색깔을 칠해보자.
    for y in range(N):
        for x in range(N):
            if area[y][x] == -1:
                Q = [(y, x)]
                area[y][x] = color
                while Q:
                    yy, xx = Q.pop()
                    area[yy][xx] = color
                    # bfs시작
                    for dy, dx in (-1, 0), (+1, 0), (0, -1), (0, +1):
                        ny = yy + dy
                        nx = xx + dx
                        # 범위 체크
                        if 0 <= ny < N and 0 <= nx < N:
                            color1 = area[ny][nx]
                            color2 = area[yy][xx]

                            weight = abs(land[ny][nx] - land[yy][xx])

                            if color1 == -1 and weight <= height:
                                Q.append((ny, nx))
                            elif color1 != -1 and color1 != color2:
                                graph.add((weight, color1, color2))
                color += 1
    global parent
    parent = [i for i in range(color)]
    graph = list(graph)
    heapq.heapify(graph)

    while graph:
        weight, color1, color2 = heapq.heappop(graph)
        if union(color1, color2):
            answer += weight

    return answer