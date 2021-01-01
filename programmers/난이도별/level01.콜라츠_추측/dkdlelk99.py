def solution(num):
    count = 0
    while num != 1:
        if num%2 == 0:
            num = num/2
            count += 1
        else:
            num = num*3 + 1
            count += 1
        if count > 500:
            return -1
    return count
    
print(solution(6) == 8)
print(solution(16) == 4)
print(solution(626331) == -1)
