from sys import stdin


def dfs(root):
    global cnt
    isTrue = False
    visit[root] = 1
    for i in range(n):
        if connection_list[root][i] == 1 and visit[i] == 0:
            isTrue = True
            dfs(i)
    if not isTrue:
        cnt += 1


n = int(stdin.readline())
input_list = list(map(int, stdin.readline().split()))
delete_node = int(stdin.readline())

connection_list = [[0] * n for i in range(n)]
visit = [0] * n
list_len = len(input_list)
cnt = 0

for i in range(list_len):
    if input_list[i] != -1:
        connection_list[i][input_list[i]] = 1
        connection_list[input_list[i]][i] = 1
    else:
        root = i
# print(connection_list)
for i in range(n):
    connection_list[delete_node][i] = 0
    connection_list[i][delete_node] = 0
# print(connection_list)
dfs(root)
if delete_node == root:
    print(0)
else:
    print(cnt)
'''
5
-1 0 0 1 1
2
'''
