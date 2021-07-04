'''
https://programmers.co.kr/learn/courses/30/lessons/72413
합승 택시 요금
[풀이]
0. 그래프 문제 중에 어려운 편.
1. 최대 요금은 100,000 이므로 각 노드 별로 도달할 수 없는 노드까지의 값을 이 보다 크게 잡는다.
=> 이 때, 100,001 로 잡으면 안된다.
=> 각 경로간의 최대 요금이 100,000 이므로 5개의 경로만 지나도 500,000 이다.
=> 지점 수 n개 만큼이 있을 때 최대로 지날 수 있는 간선의 개수는 n-1개.
=> 따라서, INF = 100,000 * (n-1) + 1 로 잡는 것이 맞다.
2. 여기서는 각 노드간의 관계를 2차원 배열로 표현했다.
=> dictionary로 표현해도 가능하다 => 이는 다익스트라 알고리즘 => 조금 더 복잡하다
3. 각 지점마다 i -> j로 가는 방법과 i -> k -> j 로 가는 방법 중 어떤 것이 최단거리 인지 비교한다
=> 플로이드 마셜 알고리즘
=> 이 때 j의 범위를 1부터 n+1로 하면 시간초과가 난다.
=> 2차원 배열 전체를 볼 게 아니라 주대각선 위의 값만 비교하면 된다.
=> board[i][j] = board[j][i] 로 양쪽 대칭값을 동시에 할당하기 때문
4. dist라는 3차원 배열을 선언한다.
=> 각각의 값은 n부터의 거리, a까지의 거리, b까지의 거리 이다.
=> n부터의 거리 : 동시에 택시를 타고 가는 거리
=> a, b부터의 거리 : 각자 택시를 타고 가는 거리
'''

def solution(n, s, a, b, fares):
    INF = (n - 1) * 100000 + 1
    board = [[INF] * (n + 1) for _ in range(n + 1)]
    for st, ed, c in fares:
        board[st][ed] = board[ed][st] = c

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                board[i][j] = board[j][i] = min(board[i][j], board[i][k] + board[k][j])

    dist = [[0, 0, 0] for _ in range(n + 1)]  # from n, a, b
    for idx in range(1, n + 1):
        board[idx][idx] = 0
        dist[idx][0] = board[s][idx]
        dist[idx][1] = board[idx][a]
        dist[idx][2] = board[idx][b]

    return min([x + y + z for x, y, z in dist if x + y + z != 0])

'''
'다익스트라 알고리즘' 으로 풀은 다른 사람의 풀이는 다음과 같다.
여기서는 2차원 배열대신 dictionary를 사용했다.

from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    dic = defaultdict(list)
    for st, ed, co in fares:
        dic[st].append((co, ed))
        dic[ed].append((co, st))
    ans = []
    for i in range(1, n+1):
        Q = [(0, i)]
        visited = [True] * (n+1)
        dp = [float('inf')] * (n+1)
        dp[i] = 0
        while Q:
            co, des = heapq.heappop(Q)
            if visited[des]:
                visited[des] = False
                for cost, destination in dic[des]:
                    dp[destination] = min(cost + dp[des], dp[destination])
                    heapq.heappush(Q, (dp[destination], destination))
        ans.append(dp[a] + dp[b] + dp[s])

    return min(ans)
'''