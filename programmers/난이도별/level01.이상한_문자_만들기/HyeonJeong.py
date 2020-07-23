#코드1
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

#코드2
def solution(s):
    answer = []
    words = s.lower().split(" ")
    for word in words:
        newWord = ""
        for i, c in enumerate(word):
            newWord += c.upper() if i % 2 == 0 else c
        answer.append(newWord)
    return " ".join(answer)

print(solution("try hello world") == "TrY HeLlO WoRlD")