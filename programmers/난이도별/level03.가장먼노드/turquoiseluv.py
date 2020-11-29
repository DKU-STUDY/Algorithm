'''
https://programmers.co.kr/learn/courses/30/lessons/49189

BFS로 노드 길이가 최대인 노드 개수 구하기
1) 주어진 노드 정보를 graph[특정 노드] = 연결된 노드 형태로 변환
    *중요! 아니면 매번 간선이 있는지 검색해야하기 때문에 런타임 오류 남
2) start 노드(now)와 인접한 노드들을 모두 save에 append
3) now가 비었으면, 다음 save와 now를 교체하여 2~3번 반복
4) save에 저장된 노드들은 모두 시작과 같은 거리의 노드들이기에, 모든 노드들이 방문되었으면 가장 마지막 save의 노드들의 개수를 반환
'''

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# return 3

def solution(n, vertex):
    graph = [[]for i in range(n+1)]
    for i in vertex:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    visited = [1] + [0]*(n)
    save = []

    start = 1
    now = [start]
    visited[start] = 1

    while now:
        start = now.pop()
        for v in graph[start]:
            if not visited[v]:
                visited[v] = 1
                save.append(v)
        if all(visited):
            return len(save)
        if not now:
            now, save = save, now

print(solution(n, vertex))
