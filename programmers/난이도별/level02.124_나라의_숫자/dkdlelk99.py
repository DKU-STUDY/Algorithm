def solution(n):
    answer = ""
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return answer
    
print(solution(1), solution(1) == '1')
print(solution(2), solution(2) == '2')
print(solution(3), solution(1) == '4')
print(solution(4), solution(1) == '11')
