def solution(x):
    s= str(x)
    sum = 0
    for i in s:
        sum += int(i)
    return True if x % sum == 0 else False

print(solution(10) == True)
print(solution(12) == True)
print(solution(11) == False)
print(solution(13) == False)
