def solution(s):
    tmp = 0
    answer = ""
    s.lower()
    for i, c in enumerate(s):
        if c == ' ':
            tmp = i+1
        if tmp == i and c.isalpha() == 1:
            answer += c.upper()
        elif  c.isalpha() == 1:
            answer += c.lower()
        else:
            answer += c
    return answer

print(solution("3people unFollowed me") == "3people Unfollowed Me", solution("for the last week") == "For The Last Week")