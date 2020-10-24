from sys import stdin
from collections import deque


def sol():
    M, N = map(int, stdin.readline().split())

    warehouse = []

    for row in range(N):
        warehouse.append(list(map(int, stdin.readline().split())))

    # print(warehouse)
    num_of_green_tomato = 0
    que = deque()
    next_append = []
    for row_idx in range(len(warehouse)):
        for ele_idx in range(len(warehouse[row_idx])):
            if warehouse[row_idx][ele_idx] == 1:
                next_append.append((ele_idx, row_idx))
            else:
                if warehouse[row_idx][ele_idx] == 0:
                    num_of_green_tomato += 1
    que.append(next_append)

    # print(f'que : {que}     ngt : {num_of_green_tomato}\n')
    time = 0
    if num_of_green_tomato == 0:
        print(time)
        return
    while len(que) > 0:
        time += 1
        current_time_search = que.popleft()
        next_append = []
        for searching_node in current_time_search:
            around_node_list = [(searching_node[0] - 1, searching_node[1]), (searching_node[0] + 1, searching_node[1]),
                                (searching_node[0], searching_node[1] - 1), (searching_node[0], searching_node[1] + 1)]
            for node in around_node_list:
                if 0 <= node[0] <= M - 1 and 0 <= node[1] <= N - 1:
                    if warehouse[node[1]][node[0]] == 0:
                        next_append.append(node)
                        warehouse[node[1]][node[0]] = 1
                        num_of_green_tomato -= 1
                        if num_of_green_tomato == 0:
                            print(time)
                            return
                continue
        if len(next_append) > 0:
            que.append(next_append)
        """print(f'current_searching_list: {current_time_search}       time: {time}\nwarehouse')
        for row in warehouse:
            print(row)
        print('\n')"""

    if num_of_green_tomato != 0:
        print(-1)


sol()
