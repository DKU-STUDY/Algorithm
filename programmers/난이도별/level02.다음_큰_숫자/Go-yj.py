'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12911
문제 : 다음 큰 숫자
값을 이진수로 바꾼 후 한글자씩 나눠 정수형으로 바꾼 후 1을 count 하였습니다.
다른 사람들 풀이를 보니 정수형으로 바꾸지 않아도 바로 count로 1을 판별할 수 있더라구요.
[메모]
n1 = bin(n).count('1')
'''

def solution(n):
    n1 = list(map(int,bin(n)[2:])).count(1)
    a, a1 = n+1, -1
    while n1 != a1 :
        a1 = list(map(int, bin(a)[2:])).count(1)
        a += 1
    return a-1
