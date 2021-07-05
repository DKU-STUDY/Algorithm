'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/72410
문제 : 신규 아이디 추천
정~말 자신없었던 정규식을 쓸 수밖에 없는 문제라서 자신없게 시작한 문제였다.
공부는 했지만 막상 적용해보니 원하는대로 결과가 안나와서 당황;;;
다른 사람들 풀이를 봐보니 정규식을 안 쓰면 훨씬훨씬 복잡해지는걸 보고
정규식 공부하라고 사이트랑 같이 리뷰 달아준 오빠한테 무한 감사를 느꼈습니다 ❁´◡`❁
'''

import re

def solution(new_id):
    new_id = new_id.lower()                     # 소문자로 변경
    new_id = re.sub("[^a-z0-9-_.]","",new_id)   # 숫자, 알파벳 소문자, 주어진 특수문자 외 나머지 삭제
    new_id = re.sub("\.{2,}",".",new_id)        # .이 2개 이상 연속할 경우 한 개로 변경
    new_id = re.sub("^\.|\.$","",new_id)        # .으로 시작하거나 .으로 끝날 경우 . 제거
    if not new_id : new_id+='a'                 # 빈 값일 경우 'a' 추가
    new_id = new_id[:15]                        # 길이 15까지로 자름
    new_id = re.sub("\.$","",new_id)            # .으로 끝날 경우 . 제거
    if len(new_id) <= 2 :                       # 길이 짧을 경우 마지막 글자 더하기
        while len(new_id) < 3 : new_id += new_id[-1]
    return new_id
