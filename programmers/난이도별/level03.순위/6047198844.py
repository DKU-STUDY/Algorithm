from collections import defaultdict

def solution(n, results):
    answer = 0
    
    wins = defaultdict(set)
    loses = defaultdict(set)
    
    for result in results:
        winner, loser = result
        wins[winner].add(loser)
        loses[loser].add(winner)
    
    for node in range(1, n+1):
        for loser in wins[node]:
            loses[loser] |= loses[node]
        
        for winner in loses[node]:
            wins[winner] |= wins[node]
    
    for node in range(1, n+1):
        if len(loses[node]) + len(wins[node]) == n-1:
            answer += 1
    
    return answer