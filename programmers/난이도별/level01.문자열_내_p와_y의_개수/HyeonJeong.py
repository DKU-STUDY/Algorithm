def solution(s):
    p_num = 0
    y_num = 0
    for c in s:
        if c in 'pP':
            p_num += 1
        elif c in 'yY':
            y_num += 1
    return p_num == y_num

print(
    solution("pPoooyY") == True,
    solution("Pyy") == False
)