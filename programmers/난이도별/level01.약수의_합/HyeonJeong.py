#처음 코드
'''
def solution(n):
    total = 0
    for i in range(1, n+1):
        if (n % i == 0):
            total += i
    return total
'''

#더 효율적인 코드
def solution(n):
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total + n

#테스트로 출력하기 위한 코드
print(solution(12))
