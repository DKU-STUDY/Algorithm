"""
시간 제한	    메모리 제한	제출	    정답	    맞은 사람	정답 비율
2 초	    256 MB	    12127	4607	3364	36.609%

문제
    트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

입력
    트리가 입력으로 주어진다.
    먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2≤V≤100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다.
    (정점 번호는 1부터 V까지 매겨져 있다고 생각한다)

    먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데,
    하나는 정점번호, 다른 하나는 그 정점까지의 거리이다.
    예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고,
    정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 입력으로 주어진다.
    주어지는 거리는 모두 10,000 이하의 자연수이다.

출력
    첫째 줄에 트리의 지름을 출력한다.
"""

# 가중치 있는 트리에서 BFS 두번 하면 되는 간단한 문제입니다.
# 트리의 지름은 임의이 노드에서 가장 먼 가중치를 가지는 노드를 찾고, 그 노드에서 다시 가장 멀리 있는 노드를 찾으면
# 그 두 노드 사이의 거리가 항상 트리의 지름인 아이디어가 핵심.

from sys import stdin
from collections import deque


def BFS(que, graph):
    md_node = 0
    md = 0
    result = {}

    while len(que) > 0:
        current_node = que.popleft()
        current_cost = que.popleft()

        if current_node not in result:
            result[current_node] = current_cost

            if current_cost > md:
                md = current_cost
                md_node = current_node
                
            for idx in range(0, len(graph[current_node]), 2):
                que += [graph[current_node][idx], graph[current_node][idx + 1] + current_cost]
    return md, md_node


def sol():
    V = int(stdin.readline())
    graph = {}
    node_list = []

    for i in range(V):
        input_list = list(map(int, stdin.readline().split()))
        node = input_list[0]
        node_list.append(node)
        graph[node] = []
        link_list = input_list[1:-1]
        graph[node] += link_list

    que = deque([node_list[0], 0])
    fst_max_distance, fst_node = BFS(que, graph)

    que = deque([fst_node, 0])
    sec_max_distance, sec_node = BFS(que, graph)
    print(sec_max_distance)
    return


sol()
