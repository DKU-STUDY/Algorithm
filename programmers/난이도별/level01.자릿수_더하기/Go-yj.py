'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12931
문제 : 자릿수 더하기
세 문제 연속으로 입력받은 자연수를 쪼개서 사용하는 문제가 나와서
절대 안 잊을 것 같아요
'''

def solution(n):
    return sum(list(map(int, str(n))))
