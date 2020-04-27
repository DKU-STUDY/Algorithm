def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    return participant[-1]

print(
    solution(['leo', 'kiki', 'eden'], ['eden', 'kiki'] ) == 'leo',
    solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola'] ) == 'vinko',
    solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']) == 'mislav'
)