from sys import stdin

global N
N = int(stdin.readline())


def DFS(start_node, graph):
    visit_list = []
    dfs_visit(start_node, visit_list, graph)
    return visit_list


def dfs_visit(node, visit_list, graph):
    current_ad_mat = graph[node - 1]
    if sum(current_ad_mat) == 0:
        visit_list.append(node)

    for idx in range(N):
        if current_ad_mat[idx] >= 1:
            graph[node - 1][idx] -= 1
            graph[idx][node - 1] -= 1
            dfs_visit(idx + 1, visit_list, graph)
    if len(visit_list) == 0:
        visit_list.append(node)
    elif visit_list[-1] != node:
        visit_list.append(node)


def solution():
    ad_mat = []
    state = True
    for _ in range(N):
        node_admat = list(map(int, stdin.readline().split()))
        if sum(node_admat) % 2 == 1:
            state = False
        ad_mat += [node_admat]
    visit_list = DFS(1, ad_mat)

    if not state:
        print(-1)
        return

    for j in ad_mat:
        if sum(j) > 0:
            print(-1)
            return

    print(str(visit_list)[1:-1])


solution()
