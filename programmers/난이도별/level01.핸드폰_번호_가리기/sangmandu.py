'''
https://programmers.co.kr/learn/courses/30/lessons/12948
핸드폰 번호 가리기
[풀이]
1. join, for 사용
'''
def solution(phone_number):
    return ''.join(['*' for i in phone_number[:-4]]) + phone_number[-4:]
'''
사실, 길이곱이 더 간단하다는 걸 생각하지 못했다니
return "*"*(len(s)-4) + s[-4:]
'''