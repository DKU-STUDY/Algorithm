def solution(x):
    return not (x % sum(map(int, str(x))))


print(solution(10) == True)
print(solution(12) == True)
print(solution(11) == False)
print(solution(13) == False)
