'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12928
문제 : 약수의 합
나머지를 사용하여 약수를 구하고 합을 반환하였습니다.
다른 사람 코드에서 이를 한 줄로 표현하는 방법이 있어 메모합니다
[메모메모]
sum([i for i in range(1,n+1) if n%i==0])
'''

def solution(n):
    answer = 0
    for i in range(1,n+1) :
        if n%i == 0 :
            answer += i
    return answer
