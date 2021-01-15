def solution(name):
    answer = 0
    locat = 0
    list = [91 - ord(n) if ord(n) > 78 else ord(n) - 65 for n in name]
    while 1:
        answer += list[locat]
        list[locat] = 0
        if sum(list) == 0: break
        left = 1
        right = 1
        while list[locat + right] == 0:
            right += 1
        while list[locat - left] == 0:
            left += 1
        if left >= right:
            locat += right
            answer += right
        else:
            locat -= left
            answer += left
    return answer

print(
    solution("JEROEN") == 56,
    solution("JAN") == 23
)

