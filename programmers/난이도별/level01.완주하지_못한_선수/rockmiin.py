def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, j in enumerate(completion):
        if j == participant[i]: continue
        elif j != participant[i]:
            return participant[i]
    return participant[-1]


print(
    solution(["leo", "kiki", "eden"], ["eden", "kiki"]),
    solution(["leo", "kiki", "eden"], ["eden", "kiki"])=="leo",
    solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'],['josipa', 'filipa', 'marina', 'nikola']),
    solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'],['josipa', 'filipa', 'marina', 'nikola'] ) == 'vinko',
    solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']),
    solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']) == 'mislav'
)