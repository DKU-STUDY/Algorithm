import heapq

V, E= map(int, input().split())
start= int(input())
INF= int(1e9)

adj= [[] for _ in range(V+1)]
distance= [INF] * (V+1)
visited= [0]* (V+1)

# 모든 간선에 대한 입력정보 입력 -> u에서 v로 가는 가중치 w인 것
for i in range(1, V+1):
    u, v, w= map(int, input().split())
    adj[u].append([v, w])

def dijkstra(start):
    q= []

    # 시작 노드 push, 값을 0으로 설정하여 입력
    # 이렇게 입력을 하면 q에서 거리가 짧은 것이 제일 먼저 pop이 될 것이다.
    heapq.heappush(q, (0, start))
    distance[start]= 0

    while q:
        # 지금 상태에서 dist가 제일 작은 값 pop
        dist, now= heapq.heappop(q)


        if distance[now]< dist:
            continue

        for i in adj[now]:
            cost= dist+ i[1]
            if cost< distance[i[0]]:
                distance[i[0]]= cost


dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF'); continue
    print(distance[i])
