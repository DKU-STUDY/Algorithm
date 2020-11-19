def solution(s):
    s=list(map(int, s.split()))
    answer=map(str, [min(s), max(s)])
    return ' '.join(answer)

solution("1 2 3 4")