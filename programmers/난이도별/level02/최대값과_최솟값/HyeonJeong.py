def solution(s):
    splitted_list = sorted(map(int, s.split()))
    return f'{splitted_list[0]} {splitted_list[-1]}'

print(
    solution("1 2 3 4") == "1 4",
    solution("-1 -2 -3 -4") == "-4 -1",
    solution("-1 -1") == "-1 -1"
)