'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12934
문제 : 정수 제곱근 판별
for문을 전부 돌려서 제곱근을 찾는 방법을 사용했습니다.
다른 사람 풀이를 보니 반복 없이 바로 제곱근을 구하더라구요
[메모메모]
sqrt = n**(1/2)
if sqrt%1==0 and (sqrt+1)**2 or -1
'''

def solution(n):
    for x in range(n+1) :
        if x**2==n : return (x+1)**2
    return -1
