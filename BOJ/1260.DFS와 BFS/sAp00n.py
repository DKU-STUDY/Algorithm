from sys import stdin
from collections import deque


def dfs(input_graph):
    global V
    dps_que = deque()
    visit = [V]
    for node in input_graph[V]:
        dps_que.append(node)
    while len(dps_que) > 0:
        #print(f'dps_visit: {visit}\ndps_que: {dps_que}')
        searching_node = dps_que.popleft()
        #print(f'current_node: {searching_node}')
        if searching_node not in visit:
            visit.append(searching_node)
            link_list = graph[searching_node]
            for idx in range(len(link_list)-1, -1, -1):
                if link_list[idx] not in visit:
                    dps_que.appendleft(link_list[idx])
    return visit


def bfs(input_graph):
    global V
    bfs_que = deque()
    visit = [V]
    for node in graph[V]:
        bfs_que.append(node)
    while len(bfs_que) > 0:
        #print(f'bfs_visit: {visit}\nbfs_que : {bfs_que}')
        searching_node = bfs_que.popleft()
        #print(f'current_node: {searching_node}')
        if searching_node not in visit:
            visit.append(searching_node)
        linked_node_list = input_graph[searching_node]
        for linked_node in linked_node_list:
            if linked_node not in visit:
                bfs_que.append(linked_node)
    return visit


global V
N, M, V = list(map(int, stdin.readline().split()))
graph = {V: []}
node_list = [V]

for _ in range(M):
    node01, node02 = list(map(int, stdin.readline().split()))
    if node01 not in graph:
        graph[node01] = []
        node_list.append(node01)
    if node02 not in graph:
        graph[node02] = []
        node_list.append(node02)
    graph[node01].append(node02)
    graph[node02].append(node01)

#print(f'node_list : {node_list}')

# print(graph)
for i in node_list:
    graph[i].sort()

#print(graph)

# DFS

DFS_result = dfs(graph)
# print(DFS_result)
DFS_str = ''
for i in range(len(DFS_result)):
    DFS_str += str(DFS_result[i])
    if i < N - 1:
        DFS_str += ' '
print(DFS_str)

# BFS
BFS_result = bfs(graph)
BFS_str = ''
for i in range(len(BFS_result)):
    BFS_str += str(BFS_result[i])
    if i < N - 1:
        BFS_str += ' '
print(BFS_str)
