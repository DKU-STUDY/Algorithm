'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12912
문제 : 두 정수 사이의 합
min, max로 a,b값을 재설정해주고 더하였습니다.
굳이 for문을 사용하지 않아도 sum 함수 안에 범위를 지정해줄 수 있더라구요
[메모]
sum(range(a,b+1))
'''

def solution(a, b):
    sum = 0
    a,b = min(a,b),max(a,b)
    for i in range(a,b+1) : sum += i
    return sum
