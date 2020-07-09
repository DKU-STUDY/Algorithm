def solution(s):
    for i in s:
        try:
            if type(int(i)) != int:
                return False
        except:
            return False
    return len(s) == 4 or len(s) == 6

print(solution('a12f') == False)
print(solution('1234') == True)
