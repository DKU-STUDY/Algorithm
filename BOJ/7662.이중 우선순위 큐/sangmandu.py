'''
https://www.acmicpc.net/problem/7662
이중 우선순위 큐 : minheap과 maxheap에서 pop하기
exist 배열을 둬서, minheap과 max
'''
from sys import stdin
import heapq as h

def solution(k):
    exist = [0] * k
    min_h, max_h = [], []
    for i in range(k):
        a, b = stdin.readline().split()
        if a == "I":
            h.heappush(min_h, (int(b), i))
            h.heappush(max_h, (-int(b), i))
            exist[i] = 1
            continue
        if b == "-1":
            while min_h and not exist[min_h[0][1]]: h.heappop(min_h)
            if min_h:
                exist[min_h[0][1]] = 0
                h.heappop(min_h)
        else:
            while max_h and not exist[max_h[0][1]]: h.heappop(max_h)
            if max_h:
                exist[max_h[0][1]] = 0
                h.heappop(max_h)

    while min_h and not exist[min_h[0][1]]: h.heappop(min_h)
    while max_h and not exist[max_h[0][1]]: h.heappop(max_h)
    if min_h and max_h: print(-max_h[0][0], min_h[0][0])
    else: print("EMPTY")

T = int(stdin.readline())
for _ in range(T):
    k = int(stdin.readline())
    solution(k)

'''
'''