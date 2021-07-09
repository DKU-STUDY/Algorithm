import bisect

def solution(A_teams, B_teams):
    answer = 0
    B_teams.sort()
    
    for A_team in A_teams:
        winner_idx =bisect.bisect(B_teams, A_team)
        # B팀이 이긴 경우. 이길수있는 비용중 최소의 비용을 들여 이긴다.
        # B팀이 무조건 지는 경우. 가장 작은 값을 내보낸다
        if winner_idx != len(B_teams):
            answer += 1
        B_teams.pop(winner_idx % len(B_teams))
        
    return answer