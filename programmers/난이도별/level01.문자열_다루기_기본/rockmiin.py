def solution(s):
    if len(s)==4 or len(s)==6:
        for i in s:
            if ord(i)>=58:
                return False
        return True
    return False

print(solution("a234")==False)