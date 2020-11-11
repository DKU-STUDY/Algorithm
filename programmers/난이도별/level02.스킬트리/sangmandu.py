'''
https://programmers.co.kr/learn/courses/30/lessons/49993
스킬트리
선후수 관계를 지켜야 하는 문자열 찾기
'''

import re
def solution(skill, skill_trees):
    order = [i+'|' for i in skill]
    match = [re.findall(''.join(order)[:-1], i) for i in skill_trees]
    return [skill[:len(i)] == ''.join(i) for i in match].count(True)

'''
'''