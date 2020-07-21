def solution(s):
    answer = ""
    for c in range(len(s)):
        if s[c] == " " :
            answer += " "
        else:
            if c % 2 == 0 :
                answer += s[c].upper()
            else:
                answer += s[c].lower()
    return answer