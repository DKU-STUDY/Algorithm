# https://www.acmicpc.net/problem/11724

"""
시간 제한	    메모리 제한	제출	    정답	    맞은 사람	    정답 비율
3 초	    512 MB	    33586	16421	10655	    46.016%

문제
    방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
    첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
    둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
    첫째 줄에 연결 요소의 개수를 출력한다.
"""

# 전체 node를 포함하는 checklist를 만들고, 거기서 방문하지 않은 노드를 뽑아 BFS를 시작하는 root 노드로 두어,
# 모든 노드를 순회할때까지 반복한다. BFS를 한번 완료할때마다 연결 요소의 개수는 +1 되는것.

from sys import stdin
from collections import deque


def bfs(que, graph, check_list):
    while len(que) > 0:
        current_node = que[0]
        link_list = graph[current_node]
        for linked_node in link_list:
            if not check_list[linked_node]:
                check_list[linked_node] = True
                que.append(linked_node)
        que.popleft()


def sol():
    N, M = map(int, stdin.readline().split())

    check_list = [True] + [False] * N
    graph = {}
    for i in range(1, N + 1):
        graph[i] = [i]

    for j in range(M):
        node01, node02 = map(int, stdin.readline().split())
        graph[node01].append(node02)
        graph[node02].append(node01)
    num_of_cc = 0
    while False in check_list:
        que = deque()
        que.append(check_list.index(False))
        bfs(que, graph, check_list)
        num_of_cc += 1
    return num_of_cc


print(sol())
