def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))


print(solution("118372") == 873211)
