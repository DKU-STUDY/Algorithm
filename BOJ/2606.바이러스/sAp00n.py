from sys import stdin
from collections import deque


def search_connected_computer(input_graph):  # for Node Num 01
    visit = {}
    stack = deque()

    for i in graph[1]:
        stack.append(i)

    number_of_connected_computer = -1
    while len(stack) > 0:
        #print(f'stack: {stack}\nvisit: {visit}')
        current_node = stack.popleft()

        if current_node in visit:
            continue

        visit[current_node] = True

        number_of_connected_computer += 1
        connected_list = graph[current_node]

        for connected_node in connected_list:
            if connected_node in visit:
                continue
            stack.append(connected_node)
    return number_of_connected_computer


Num_of_computers = int(stdin.readline())
Num_of_connection = int(stdin.readline())

graph = {}

for i in range(1, Num_of_computers + 1):
    graph[i] = []

for i in range(Num_of_connection):
    computer01, computer02 = list(map(int, stdin.readline().split()))
    graph[computer01].append(computer02)
    graph[computer02].append(computer01)

#print(graph)
num_of_com = search_connected_computer(graph)

print(num_of_com)