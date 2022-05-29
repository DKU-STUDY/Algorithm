import heapq

PQ = []
for i in range(1, 8+1):
    heapq.heappush(PQ, (-int(input()), i))

res = []
s = 0
for i in range(5):
    k, l = heapq.heappop(PQ)
    res.append(l)
    s -= k
print(s)
res.sort()
for i in res:
    print(i, end=' ')