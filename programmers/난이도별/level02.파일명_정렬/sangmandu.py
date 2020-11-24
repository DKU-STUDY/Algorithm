'''
https://programmers.co.kr/learn/courses/30/lessons/17686
파일명 정렬
정규식 사용. 이후 3개의 부분으로 분리 후 정렬. 공백도 문자라는 것을 주의
'''

import re
def solution(files):
    head = re.compile('[-. a-zA-z]+')
    number = re.compile('[0-9]+')

    newfiles = []
    for file in files:
        _, h = re.search(head, file).span()
        _, n = re.search(number, file).span()
        newfiles.append([file[:h], file[h:n], file[n:]])

    return [''.join(i) for i in sorted(newfiles, key=lambda f: (f[0].lower(), int(f[1])))]

'''
re.search 대신 findall을 사용할 수 있음
[-. a-zA-z]대신 \d를 사용할 수 있음
'''