def solution(s, n):
    answer = ""
    for i in s:
        if i == " ":
            answer += " "
        else:
            start = ord('A') if i.isupper() else ord('a')
            answer += chr((ord(i) - start + n) % 26 + start)
    return answer

print(
    solution("AB", 1) == "BC",
    solution("z", 1) == "a",
    solution("a B z", 4) == "e F d"
)


