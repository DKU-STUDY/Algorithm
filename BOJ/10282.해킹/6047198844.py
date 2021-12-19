# 현시점
import heapq
import sys
from collections import defaultdict

T = int(sys.stdin.readline())
for _ in range(T):
    # 컴퓨터 대수 / 의존성 개수 / 해킹당한 컴퓨터 번호
    n, d, c = map(int, sys.stdin.readline().split())

    edges = defaultdict(list)
    for __ in range(d):
        # b가 감염시 s초 후에 a가 감염된다.
        a, b, s = map(int, sys.stdin.readline().split())
        edges[b].append((s, a))

    PQ = []
    for s, pc in edges[c]:
        heapq.heappush(PQ, (s, pc))

    # 현재 시각
    cur = 0
    hacked_pc_num = 1
    visited_pc = set()
    visited_pc.add(c)
    while PQ:
        s, hacked_pc = heapq.heappop(PQ)
        if hacked_pc in visited_pc:
            continue
        hacked_pc_num += 1
        cur = s

        visited_pc.add(hacked_pc)
        for s, pc in edges[hacked_pc]:
            heapq.heappush(PQ, (s + cur, pc))

    print(hacked_pc_num, cur)
