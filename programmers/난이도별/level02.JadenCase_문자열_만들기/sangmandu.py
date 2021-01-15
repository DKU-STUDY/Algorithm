'''
https://programmers.co.kr/learn/courses/30/lessons/12951
JadenCase 문자열 만들기
'''

import re
def solution(s):
    idx = [i.span()[1]-1 for i in re.finditer('\s\w', s)]
    s = list(s[0].upper()+s[1:].lower())
    for i in idx:
        s[i] = s[i].upper()
    return ''.join(s)


'''
처음에는 아래처럼 풀었는데, 공백의 크기도 고려해야 해서 결국 split을 사용하지 못했다.
def solution(s):
    return ''.join(map(lambda x : str(x[0]).upper()+x[1:].lower()+' ', s.split()))[:-1]

정규식을 안쓰더라도 다음과 같이 간단하게 할 수 있었을 것 같긴하다. 라이브러리 의존도가 높아진 느낌
def solution(s):
    line = s[0].upper()
    for idx, c in enumerate(s[1:]):
        if s[idx-1] == " ":
            line += s[idx].upper()
        else:
            line += s[idx].lower()
    return line
'''