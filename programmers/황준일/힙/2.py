# https://programmers.co.kr/learn/courses/30/lessons/42629
# 현재 공장에 남아있는 밀가루 수량 stock
# 밀가루 공급 일정(dates)
# 해당 시점에 공급 가능한 밀가루 수량(supplies)
# 원래 공장으로부터 공급받을 수 있는 시점 k
# 밀가루가 떨어지지 않고 공장을 운영하기 위해서 최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지
from heapq import heappush as push, heappop as pop

# 테스트 1 〉	통과 (2.25ms, 22.3MB)
# 테스트 2 〉	통과 (0.53ms, 18.1MB)
# 테스트 3 〉	통과 (0.74ms, 11.7MB)
def solution(stock, d, s, k):
    h = []
    d += [k]
    s += [0]
    cnt = i = 0
    for now in d :
        push(h, -s[i])
        i += 1
        while stock <= now :
            stock -= pop(h)
            cnt += 1
            if stock >= k : return cnt

print(solution(4, [4, 10, 15], [20, 5, 10], 30))