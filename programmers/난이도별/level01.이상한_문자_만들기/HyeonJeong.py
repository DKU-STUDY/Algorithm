def solution(s):
    answer = ""
    list = s.split(" ")
    for n in list:
        for m in range(len(list[n])):
            str = list[n][m]
            if "a" <= str <= "z" and c % 2 == 0:
                answer += str.upper()
            elif "A" <= str <= "Z" and c % 2 == 1:
                answer += str.lower()
            else:
                answer += str
        answer += " "
    return answer