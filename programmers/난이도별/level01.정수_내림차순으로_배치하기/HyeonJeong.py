def solution(n):
    answer = list(str(n) #answer = [c for c in str(n)]
    answer.sort(reverse = True)
    return int("".join(answer))

    #한줄로는 return int("".join(sorted(list(str(n)), reverse = True)))
print(solution(118372) == 873211)