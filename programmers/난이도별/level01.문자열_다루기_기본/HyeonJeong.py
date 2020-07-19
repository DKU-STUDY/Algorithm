def solution(s):
    if len(s) == 4 or 6 :
        list(s)
        for i in s :
            if s[i] in "0123456789":
                answer = True
    else :
        answer = False
    return answer
