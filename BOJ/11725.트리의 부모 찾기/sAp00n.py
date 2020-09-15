from sys import stdin
from collections import deque


def bfs_searching(graph):
    stack = deque()
    visit = {}
    memo = {1: None}
    for node in graph[1]:
        stack.append(node)
        memo[node] = 1
    while len(stack) > 0:
        searching_node = stack.popleft()
        #print(f'searching_node : {searching_node}\nvisit : {visit}\nstack: {stack}')
        if searching_node in visit:
            continue
        visit[searching_node] = True
        for node in graph[searching_node]:
            if node not in memo:
                memo[node] = searching_node
                #print(f'searching_node : {searching_node}\nnode: {node}\nmemo : {memo}')
            if node in visit:
                continue
            stack.append(node)
    return memo


number_of_nodes = int(stdin.readline())
graph = {1: []}

for connection in range(number_of_nodes - 1):
    node01, node02 = list(map(int, stdin.readline().split()))
    if node01 not in graph:
        graph[node01] = []
    if node02 not in graph:
        graph[node02] = []
    graph[node01].append(node02)
    graph[node02].append(node01)
#print(f'graph : {graph}')


parent_node = bfs_searching(graph)
#print(parent_node)

for i in range(2, number_of_nodes + 1):
    print(parent_node[i])
