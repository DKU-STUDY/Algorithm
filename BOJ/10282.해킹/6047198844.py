# 현시점
import heapq
from collections import defaultdict

T = int(input())
for _ in range(T):
    # 컴퓨터 대수 / 의존성 개수 / 해킹당한 컴퓨터 번호
    n, d, c = map(int, input().split())

    edges = defaultdict(list)
    for __ in range(d):
        # b가 감염시 s초 후에 a가 감염된다.
        a, b, s = map(int, input().split())
        edges[b].append((s, a))

    PQ = []
    for s, pc in edges[c]:
        heapq.heappush(PQ, (s, pc))

    # 현재 시각
    cur = 0
    hacked_pc_num = 1
    while PQ:
        hacked_pc_num += 1

        s, hacked_pc = heapq.heappop(PQ)
        cur += s

        for pc, s in edges[hacked_pc]:
            heapq.heappush(PQ, (s + cur, pc))

    print(hacked_pc_num, cur)
