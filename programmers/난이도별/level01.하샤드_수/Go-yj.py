'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12947
문제 : 하샤드 
10으로 나눈 나머지를 계속 더함으로써 각 자리수의 합을 구했습니다.
다른 사람 풀이를 보니 한 줄만으로도 자릿수의 합을 구할 수 있었습니다.
[메모메모]
x % sum([int(c) for c in str(x)])
'''

def solution(x):
    answer = True
    sum = 0
    num = x
    for i in range(len(str(x))) :
        sum += num%10
        num //= 10
    if x%sum != 0 :
        answer = False
    return answer
