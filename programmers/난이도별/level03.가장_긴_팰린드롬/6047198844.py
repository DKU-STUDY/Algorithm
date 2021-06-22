def solution(s):
    for l in range(len(s),0,-1):
        for i in range(0,len(s)-l+1):
            if s[i:i+l] == s[i:i+l][::-1]:
                return l