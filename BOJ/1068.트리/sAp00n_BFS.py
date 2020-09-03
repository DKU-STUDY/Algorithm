from sys import stdin
from collections import deque


def BFS(connection_list, n):
    leaf_node_num = 0
    stack = deque()
    visit = {}
    stack.append(0)
    while len(stack) > 0:
        temp = stack.popleft()
        for i in range(n):
            if connection_list[temp][i] == 1:
                connection_list[i][temp] = 0
        # print(f'temp : {temp}')
        visit[temp] = None
        if 1 not in connection_list[temp]:
            leaf_node_num += 1
        else:
            for i in range(len(connection_list[temp])):
                if connection_list[temp][i] == 1 and i not in visit:
                    stack.append(i)
        # print(stack)
    return leaf_node_num


def solution(n, input_list, del_node):
    if del_node == 0:
        return 0
    connection_list = [[0] * n for _ in range(n)]
    visit = [0] * n

    for i in range(n):
        if input_list[i] == -1:
            pass
        else:
            connection_list[input_list[i]][i] = 1
            connection_list[i][input_list[i]] = 1
    for i in range(n):
        if connection_list[del_node][i] == 1:
            connection_list[del_node][i] = 0
            connection_list[i][del_node] = 0

    # print(f'connection_list: {connection_list}')
    leaf_num = BFS(connection_list, n)

    return leaf_num


n = int(stdin.readline())
input_list = list(map(int, stdin.readline().split()))
del_node = int(stdin.readline())

print(solution(n, input_list, del_node))


