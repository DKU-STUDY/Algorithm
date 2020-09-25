def solution(s):
    tmp = 0
    answer = ""
    list = []
    for i, c in enumerate(s.lower()):
        if c == ' ':
            tmp = i+1
        answer += c.upper() if tmp == i and c.isalpha() == 1 else c
    return answer

print(
    solution("3people unFollowed me") == "3people Unfollowed Me",
    solution("for the last week") == "For The Last Week"
)