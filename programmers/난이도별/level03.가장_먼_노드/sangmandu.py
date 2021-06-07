'''
https://programmers.co.kr/learn/courses/30/lessons/49189
가장 먼 노드
[풀이]
1에서 부터 bfs로 접근하고 이에 따라서 거리를 +1씩 부여하는 방법
시간초과 이슈에 대해서는 간선을 조사할 때 행렬이 아니라 딕셔너리로 조사
'''
from collections import defaultdict
def solution(n, edge):
    board = defaultdict(list)
    dist = [0, 0.5] + [0] * (n - 1)

    for st, ed in edge:
        board[st].append(ed)
        board[ed].append(st)

    stack = [1]
    save = []
    distance = 1
    while True:
        if not stack:
            if not save:
                return dist.count(max(dist))
            distance += 1
            save, stack = stack, save

        st = stack.pop()
        for idx in board[st]:
            if dist[idx] == 0:
                dist[idx] = distance
                save.append(idx)

'''
'''