def solution(s, n):
    answer = ""
    for i in s:
        if i == " ":
            answer += " "
        elif ('A' <= i <= 'Z' and ord(i) + n > 90) or ('a' <= i <= 'z' and ord(i) + n > 122):
            answer += chr(ord(i) - 26 + n)
        else:
            answer += chr(ord(i) + n)
    return answer

print(
    solution("AB", 1) == "BC",
    solution("z", 1) == "a",
    solution("a B z", 4) == "e F d"
)

