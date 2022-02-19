import heapq
import sys

N, K = map(int, sys.stdin.readline().split())
diamonds = [tuple(map(int, sys.stdin.readline().split()))for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]
# 최대한 작은 가방을 가지고, 최대한 비싼 다이아몬드를 담는다.
diamonds.sort()
bags.sort()

# 임시큐.
Q = []

diamond_idx = 0
res = 0

for bag in bags:
    # 허용되는 다이아몬드를 담는다. 이때 diamond_idx 를 유지시킨다.
    # Q 는 항상 가장 값어치 있는 다이아몬드를 가리킨다.
    while diamond_idx < N and diamonds[diamond_idx][0] <= bag:
        heapq.heappush(Q, (-diamonds[diamond_idx][1], diamonds[diamond_idx][1]))
        diamond_idx += 1
    if Q:
        res += heapq.heappop(Q)[1]
    # Q 의 맨위에는 가장 값어치 있는 다이아몬드가 있다.
    # 이 다이아몬드는 현재 가방의 무게에 맞는다.
        # 근거
        # 이전의 가방이 낮은 무게를 허용하는 가방이기 때문에 현재가방은 당연히 클수밖에 없다.
        # 우선순위큐의 정의에 의해서 가장 값어치있음이 보장된다.
print(res)