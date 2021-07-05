#다시
#접근이 잘못됬음
def solution(n, s):
    num = s // n
    return [-1] if num == 0 else [num] * (n-s%n) + [num+1] * (s%n)