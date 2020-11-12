'''
https://programmers.co.kr/learn/courses/30/lessons/17682
전화번호 목록 : 접두사 찾기
re 정규식 사용
'''

import re
def solution(phone_book):
    for i in phone_book:
        for j in phone_book:
            if i == j: continue
            if re.match(i, j) != None: return False
    return True


'''
'''