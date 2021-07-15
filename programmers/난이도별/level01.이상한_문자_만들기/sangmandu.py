'''
https://programmers.co.kr/learn/courses/30/lessons/12930
이상한 문자 만들기
[풀이]
1. split, upper, lower
'''
def solution(s):
    words = s.split(' ')
    answer = ''
    for word in words:
        for i, v in enumerate(word):
            answer += v.upper() if i % 2 == 0 else v.lower()
        answer += ' '
    return answer[:-1]
'''
마지막에 공백을 추가하는 방법 대신 ' '.join() 을 사용할 수 있음
return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])
'''