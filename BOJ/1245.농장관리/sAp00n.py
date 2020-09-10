from sys import stdin
from collections import deque


def near_check(mat, node):
    global N_Column
    global M_Row

    i, j = node
    node_val = mat[j][i]
    return_list = []
    if i == 0:
        if j == 0:
            search_list = [[i + 1, j], [i, j + 1], [i + 1, j + 1]]
            for near_node in search_list:
                near_i, near_j = near_node
                if near_i <= M_Row - 1 and near_j <= N_Column - 1:
                    if mat[near_j][near_i] <= node_val:
                        return_list.append([near_i, near_j])

        elif j == N_Column - 1:
            search_list = [[i + 1, j], [i, j - 1], [i + 1, j - 1]]
            for near_node in search_list:
                near_i, near_j = near_node
                if near_i <= M_Row -1 and near_j <= N_Column - 1:
                    if mat[near_j][near_i] <= node_val:
                        return_list.append([near_i, near_j])
        else:
            search_list = [[i, j - 1], [i + 1, j - 1], [i + 1, j], [i + 1, j + 1], [i, j + 1]]
            for near_node in search_list:
                near_i, near_j = near_node
                if near_i <= M_Row - 1 and near_j <= N_Column -1:
                    if mat[near_j][near_i] <= node_val:
                        return_list.append([near_i, near_j])

    elif i == M_Row - 1:
        if j == 0:
            search_list = [[i - 1, j], [i - 1, j + 1], [i, j + 1]]
            for near_node in search_list:
                near_i, near_j = near_node
                if near_i <= M_Row - 1 and near_j <= N_Column - 1:
                    if mat[near_j][near_i] <= node_val:
                        return_list.append([near_i, near_j])
        elif j == N_Column - 1:
            search_list = [[i - 1, j], [i - 1, j - 1], [i, j - 1]]
            for near_node in search_list:
                near_i, near_j = near_node
                if near_i <= M_Row - 1 and near_j <= N_Column - 1:
                    if mat[near_j][near_i] <= node_val:
                        return_list.append([near_i, near_j])
        else:
            search_list = [[i, j - 1], [i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j + 1]]
            for near_node in search_list:
                near_i, near_j = near_node
                if near_i <= M_Row - 1 and near_j <= N_Column - 1:
                    if mat[near_j][near_i] <= node_val:
                        return_list.append([near_i, near_j])

    else:
        if j == 0:
            search_list = [[i - 1, j], [i - 1, j + 1], [i, j + 1], [i + 1, j + 1], [i + 1, j]]
            for near_node in search_list:
                near_i, near_j = near_node
                if near_i <= M_Row - 1 and near_j <= N_Column -1:
                    if mat[near_j][near_i] <= node_val:
                        return_list.append([near_i, near_j])
        elif j == N_Column - 1:
            search_list = [[i - 1, j], [i - 1, j - 1], [i, j - 1], [i + 1, j - 1], [i + 1, j]]
            for near_node in search_list:
                near_i, near_j = near_node
                if near_i <= M_Row - 1 and near_j <= N_Column - 1:
                    if mat[near_j][near_i] <= node_val:
                        return_list.append([near_i, near_j])
        else:
            search_list = [[i - 1, j], [i - 1, j - 1], [i, j - 1], [i + 1, j - 1], [i + 1, j], [i + 1, j + 1],
                           [i, j + 1], [i - 1, j + 1]]
            for near_node in search_list:
                near_i, near_j = near_node
                if near_i <= M_Row - 1 and near_j <= N_Column - 1:
                    if mat[near_j][near_i] <= node_val:
                        return_list.append([near_i, near_j])
    return return_list


N_Column, M_Row = list(map(int, stdin.readline().split()))

if N_Column == 1 and M_Row == 1:
    if int(stdin.readline()) != 0:
        print(1)
    else:
        print(0)
else:
    mat = [None] * N_Column
    num_of_Mount = 0

    for j in range(N_Column):
        mat[j] = list(map(int, stdin.readline().split()))

    graph = {}
    max_val = 0
    for j in range(N_Column):
        for i in range(M_Row):
            ele = mat[j][i]
            if ele not in graph:
                graph[ele] = []
            graph[ele] += [[i, j]]
            max_val = max(max_val, ele)

    for value in range(max_val, 0, -1):
        same_value_node_list = graph.get(value)

        if same_value_node_list is None:
            continue

        for searching_node in same_value_node_list:
            searching_i, searching_j = searching_node
            if mat[searching_j][searching_i] == 0:
                continue
            stack = deque()
            stack.append([searching_i, searching_j])

            while len(stack) > 0:
                current_node = stack.popleft()
                #print(f'stack: {stack}')
                current_i, current_j = current_node
                #print(f'current : ({current_i}, {current_j}) = {mat[current_j][current_i]}')
                if mat[current_j][current_i] == 0:
                    continue
                near_node_list = near_check(mat, current_node)
                #print(f'near_node : {near_node_list}')
                for node in near_node_list:
                    node_i, node_j = node

                    if mat[node_j][node_i] == 0:
                        continue

                    if mat[current_j][current_i] >= mat[node_j][node_i]:
                        stack.append(node)
                        #print(f'append node : ({node_i}, {node_j})')
                mat[current_j][current_i] = 0
            num_of_Mount += 1

        '''for i in mat:
            print(i)
        print('\n')'''

    print(num_of_Mount)
