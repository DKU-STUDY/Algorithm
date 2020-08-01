def solution(phone_number):
    answer = ""
    for i, c in enumerate(phone_number):
        answer += "*" if i < len(phone_number) - 4 else c
    return answer