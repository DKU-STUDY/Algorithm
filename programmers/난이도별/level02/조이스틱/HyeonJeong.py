def solution(name):
    answer = 0
    if name == "AAA" or name == "AAAA":
        return answer
    for n in name:
        if ord(n) > 78:
            answer += 91 - ord(n) # 이전 알파벳으로
        else:
            answer += ord(n) - 65 # 다음 알파벳으로
        answer += 1 # 커서 다음으로 이동
    answer -= 1 # 마지막 알파벳 완성할 때 위의 이동 필요 없으므로
    if name[-1]  == 'A' or name[1] == 'A':
        if name[-1:-3] or name[1:3] == "AA":
            answer -= 2
        elif name[1:] == "AAA":
            answer -= 3
        else:
            answer -= 1
    return answer

print(
    solution("JEROEN") == 56,
    solution("JAN") == 23
)

