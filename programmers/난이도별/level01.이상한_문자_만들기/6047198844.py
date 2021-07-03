def solution(s):
    answer = ''

    idx = 0
    for char in s:
        if char == ' ':
            idx = 0
            answer += char
            continue
        if idx % 2 == 0:
            answer += str.upper(char)
        else:
            answer += str.lower(char)
        idx += 1

    return answer

# 공백이 여러개라면?