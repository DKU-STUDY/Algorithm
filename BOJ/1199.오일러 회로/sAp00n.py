from sys import stdin
from collections import deque

def dfs(graph):
    que = deque()
    visit = {}
    que.append(1)
    while len(que) > 0:
        current_node = que.pop()



N = int(stdin.readline())

graph = {}

for i in range(1, N+1):
    graph[i] = []
    input_list = list(map(int, stdin.readline().split()))
    for ele_idx in range(len(input_list)):
        if input_list[ele_idx] == 1:
            graph[i].append(ele_idx + 1)

print(graph)