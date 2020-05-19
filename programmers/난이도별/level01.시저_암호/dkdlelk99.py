def solution(s, n):
    small = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    big = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    answer = []
    for c in s :
        if (c.isspace()):
            answer += c
            continue
        target = small if c.islower() else big
        answer += target[(target.index(c) + n) % 26]
    return ''.join(answer)

print(solution('sdf Z',1) == 'teg A')
print(solution('a B z',4) == 'e F d')
