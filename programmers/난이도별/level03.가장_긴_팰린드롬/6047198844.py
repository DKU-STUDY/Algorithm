def solution(s):
    for l in range(len(s),0,-1):
        for i in range(0,len(s)-l+1):
            check = s[i:i+l]
            if check == check[::-1]:
                return l