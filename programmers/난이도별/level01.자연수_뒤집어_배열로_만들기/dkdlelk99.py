def solution(n):
    s = str(n)
    answer = [int(i) for i in s]
    answer.reverse()
    return answer

print(solution(19) == [9, 1])
print(solution(12345) == [5,4,3,2,1])
