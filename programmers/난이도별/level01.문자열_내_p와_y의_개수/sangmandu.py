'''
https://programmers.co.kr/learn/courses/30/lessons/12916
문자열 내 p와 y의 개수 : P,p와 Y,y의 개수 비교
count
'''

def solution(s):
    return s.count('p') + s.count('P') == s.count('y') + s.count('Y')

'''
대소문자 무관하게 비교 할 때는 lower() 또는 upper() 사용하기
return s.lower().count('p') == s.lower().count('y')
'''