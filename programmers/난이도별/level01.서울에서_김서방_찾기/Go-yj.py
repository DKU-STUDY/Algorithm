'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12919
문제 : 서울에서 김서방 찾기
index 함수를 사용해서 Kim이 있는 index를 찾아 반환하였습니다.
반환할 때 저는 string을 +로 합쳐서 반환하였는데
다른 사람들 코드에서 format을 사용하는 게 많아 잊지 않으려고 메모합니다.
[메모]
'김서방은 {}에 있다'.format(seoul.index("Kim"))
'''

def solution(seoul):
    return '김서방은 '+str(seoul.index("Kim"))+'에 있다'
