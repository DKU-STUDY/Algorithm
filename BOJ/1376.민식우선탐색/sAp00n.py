from sys import stdin


def mFS(graph):
    global N
    current_node = 1
    visit_list = []
    checker = {}
    while len(visit_list) < N:
        # print(f'visit_list : {visit_list}')
        temp = graph[current_node]
        connected_list = []
        for node in temp:
            if node in checker:
                continue
            connected_list.append(node)
        # print(f'current : {current_node}        connect: {connected_list}')

        if current_node in checker and len(connected_list) == 0:
            current_node = visit_list[visit_list.index(current_node) - 1]
            continue

        if len(connected_list) == 0:

            if current_node not in checker:
                visit_list.append(current_node)
                checker[current_node] = True

            current_node = visit_list[visit_list.index(current_node) - 1]

        elif len(connected_list) == 1:

            if current_node not in checker:
                visit_list.append(current_node)
                checker[current_node] = True

            current_node = connected_list[0]

        elif len(connected_list) % 2 == 1:

            if current_node not in checker:
                visit_list.append(current_node)
                checker[current_node] = True

            current_node = connected_list[len(connected_list) // 2]

        else:

            if current_node not in checker:
                visit_list.append(current_node)
                checker[current_node] = True

            current_node = connected_list[0]

    return visit_list


global N
N, M = list(map(int, stdin.readline().split()))

graph = {}
checker = {}
for i in range(1, N + 1):
    graph[i] = []
    checker[i] = {}

for _ in range(M):
    node01, node02 = list(map(int, stdin.readline().split()))
    if node01 == node02:
        continue
    if node02 not in checker[node01]:
        graph[node01].append(node02)
        checker[node01][node02] = True
    if node01 not in checker[node02]:
        graph[node02].append(node01)
        checker[node02][node01] = True

for i in range(1, N + 1):
    graph[i].sort()

#print(graph)
#print(checker)
visit_list = mFS(graph)
return_str = ''

for node in visit_list:
    return_str += str(node) + ' '
print(return_str[:-1])
