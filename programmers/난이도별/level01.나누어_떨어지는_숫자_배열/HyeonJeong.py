# 1차
def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer += [a]
    if answer == []:
        answer += [-1]
    answer.sort(reverse = False)
    return answer

# 2차
def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer += [a]
    return sorted(answer) if answer != [] else [-1]

# 3차
def solution(arr, divisor):
    answer = [a for a in arr if a % divisor == 0]
    return sorted(answer) if answer != [] else [-1]