import sys


# 입력
members = sys.stdin.readlines()
# i번째 선수 / white 팀의 맴버수 / black 팀의 맴버수
# i는 1부터 시작한다.
memo = [[[0 for _ in range(15+1)] for _ in range(15+1)] for _ in range(len(members)+1)]
for idx, member in enumerate(members):
    for white in range(15 + 1):
        for black in range(15 + 1):
            white_ability, black_ability = map(int, member.split())
            # i번째 선수를 white 팀에 속하게 함.
            if white + 1 <= 15:
                memo[idx+1][white+1][black] = max(memo[idx+1][white+1][black], memo[idx][white][black] + white_ability)
            # i번째 선수를 black 팀에 속하게 함.
            if black + 1 <= 15:
                memo[idx+1][white][black+1] = max(memo[idx+1][white][black+1], memo[idx][white][black] + black_ability)
            # i번째 선수를 아무팀에도 속하지 않게함.
            memo[idx + 1][white][black] = max(memo[idx + 1][white][black], memo[idx][white][black])

print(memo[len(memo)-1][15][15])