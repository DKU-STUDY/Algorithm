'''
https://programmers.co.kr/learn/courses/30/lessons/12918
문자열 다루기 기본
[풀이]
1. 문자열의 길이가 4 또는 6이면서 숫자로만 구성하기
2. str을 int casting 할 때의 에러로 구분.
'''
def solution(s):
    try: return str(int(s)) == s and (len(s) == 4 or len(s) == 6)
    except: return False
''' 
isalpha와 isdigit을 사용하면 쉽게 문자열의 문자, 숫자 판단을 할 수 있다.
or 을 이용한 비교 보다는 in (4, 6)으로 비교하면 간단하다.

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
'''