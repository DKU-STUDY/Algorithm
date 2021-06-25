def solution(a, b):
    if a > b:
        return solution(b, a)
    return sum(range(a,b+1))