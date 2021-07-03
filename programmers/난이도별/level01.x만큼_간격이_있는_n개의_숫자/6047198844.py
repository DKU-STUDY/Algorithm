def solution(x, n):
    return list(range(x,x*n+x,x)) if x != 0 else [0 for _ in range(n)]