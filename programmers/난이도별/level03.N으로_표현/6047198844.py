#bottom - up방식으로 풀어보기
from collections import defaultdict

def solution(N, number):    
    memo = defaultdict(set)
    
    for i in range(1,8+1):
        memo[i].add(int(str(N)*i))
    
    #N을 times번 사용해서 얻을수있는 값들을 리턴한다.
    def dp(times, N):
        if len(memo[times]) != 1 or times == 1:
            return memo[times]
        
        for t in range(1,times):
            for s in dp(times-t,N):
                for u in dp(t,N):
                    if s + u != 0:
                        memo[times].add(s + u)
                    if s - u != 0:
                        memo[times].add(s - u)
                    if s // u != 0:
                        memo[times].add(s // u)
                    if s * u != 0:
                        memo[times].add(s * u)        
        return memo[times]
        
    dp(8,N)

    for key, value in sorted(memo.items()):
        if number in value:
            return key
    return -1