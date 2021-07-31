'''
문자열 압축
https://programmers.co.kr/learn/courses/30/lessons/60057
'''
def solution(s):
    size = len(s)
    answer = size
    for i in range(1, size):
        top = s[:i]
        newStr = ""
        cnt = 1
        for j in range(1, size // i + (1 if size % i == 0 else 2)):
            if top == s[i*j:i*(j+1)]:
                cnt += 1
                continue
            if cnt >= 2:
                newStr += str(cnt)
            newStr += str(top)
            top = s[i*j:i*(j+1)]
            cnt = 1
        answer = min(answer, len(newStr))
    return answer
'''
'''