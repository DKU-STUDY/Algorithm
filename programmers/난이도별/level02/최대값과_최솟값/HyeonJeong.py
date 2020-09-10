def solution(s):
    list = [int(i) for i in s.split(' ')]
    return str(min(list)) + ' ' + str(max(list))

print(
    solution("1 2 3 4") == "1 4",
    solution("-1 -2 -3 -4") == "-4 -1",
    solution("-1 -1") == "-1 -1"
)