def solution(participant, completion):
    vector = {}
    for v in participant : vector[v] = vector.get(v, 0) + 1
    for v in completion :
        vector[v] -= 1
        if vector[v] == 0 : del vector[v]
    for k, v in vector.items() :
        return k

print(
    solution(['leo', 'kiki', 'eden'], ['eden', 'kiki'] ) == 'leo',
    solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola'] ) == 'vinko',
    solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']) == 'mislav'
)