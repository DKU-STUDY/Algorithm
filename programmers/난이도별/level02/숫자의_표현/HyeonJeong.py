import math
def solution(n):
    answer = 0
    for i in range(1, math.ceil(n/2)):
        total = 0
        for j in range(i, n):
            total += j
            if total >= n:
                if total == n:
                    answer += 1
                break
    return answer + 1 # n = n

print(solution(15) == 4)