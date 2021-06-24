'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12916
문제 : 문자열 내 p와 y의 개수
count() 함수를 이용해서 p와 y의 개수를 구하고 비교하였습니다.
if문을 사용하여 판별하고 return 하였는데
다른 사람 코드를 보니 단순히 한 줄로 True, False를 판별하고 반환할 수 있네요
[메모]
return s.lower().count('p') == s.lower().count('y')
'''

def solution(s):
    p = s.count('p') + s.count('P')
    y = s.count('y') + s.count('Y')
    return True if p==y else False
