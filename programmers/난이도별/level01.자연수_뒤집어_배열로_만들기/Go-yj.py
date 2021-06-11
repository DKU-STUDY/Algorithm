'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12932
문제 : 자연수 뒤집어 배열로 만들기
쪼개고 역순을 취하는 방법을 사용했습니다.
한 줄로 할려니까 아직은 잘 안되더라구요
다른 사람 풀이 봤더니 저는 두 개의 별개의 식을 이어붙인 느낌인데
정말 깔끔한 한줄로 했길래 기억할려구 적어봅니다
[메모메모]
list(map(int, reversed(str(n))))
'''

def solution(n):
    return list(reversed(list(map(int, str(n)))))
