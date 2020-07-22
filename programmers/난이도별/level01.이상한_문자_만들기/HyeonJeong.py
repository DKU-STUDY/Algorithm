def solution(s):
    answer = ""
    words = s.split(" ")
    for i in range(len(words)):
        for j in range(len(words[i])):
            c = words[i][j]
            if "a" <= c <= "z" and j % 2 == 0:
                answer += c.upper()
            elif "A" <= c <= "Z" and j % 2 == 1:
                answer += c.lower()
            else:
                answer += c
        if i < len(words) - 1:
            answer += " "
    return answer

print(solution("try hello world") == "TrY HeLlO WoRlD")