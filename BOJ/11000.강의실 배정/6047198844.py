import heapq
import sys

PQ = []
# 종료시간을 저장. 각각은 하나의 강의실을 의미한다.
PQF = []

N = int(sys.stdin.readline())
for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    heapq.heappush(PQ, (S, T))

while PQ:
    S, T = heapq.heappop(PQ)

    if not PQF:
        heapq.heappush(PQF, T)
        continue

    # 종료시간이 가장 빠른 강의실의 종료시간이 새로 추가하려는 강의시간보다 같거나 빠른 경우
    # 해당 강의실에서 이어 강의할수있다. 따라서 해당 강의실을 POP하고 추가한다.
    if PQF[0] <= S:
        heapq.heappop(PQF)
    heapq.heappush(PQF, T)
print(len(PQF))
