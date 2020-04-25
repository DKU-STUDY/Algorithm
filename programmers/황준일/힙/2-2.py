# https://programmers.co.kr/learn/courses/30/lessons/42629
# 현재 공장에 남아있는 밀가루 수량 stock
# 밀가루 공급 일정(dates)
# 해당 시점에 공급 가능한 밀가루 수량(supplies)
# 원래 공장으로부터 공급받을 수 있는 시점 k
# 밀가루가 떨어지지 않고 공장을 운영하기 위해서 최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지
from heapq import heappush as push, heappop as pop

def solution(stock, d, s, k):
    cnt = 0
    i = 0
    last = len(d)
    h = []
    for now in range(k):
        if i < last and now == d[i]:
            push(h, -s[i])
            i+=1
        if not stock or (h and stock - h[0] >= k - 1):
            stock = -pop(h)
            cnt += 1
            if stock >= k - now : return cnt
        stock -= 1

print(solution(4, [4, 10, 15], [20, 5, 10], 30))