'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12918
문제 : 문자열 다루기 기본
파이썬 예외처리를 이용해서 int로 바꿀 때 error가 나면 false를 반환해주도록 했습니다.
다른 사람 풀이를 보니 isdigit()이라는 유용한 함수가 있어 기록합니다.
[메모]
return s.isdigit() and len(s) in (4,6)
'''

def solution(s):
    if len(s)==4 or len(s)==6 :
        try :
            n = int(s)
        except :
            return False
    else :
        return False
    return True
