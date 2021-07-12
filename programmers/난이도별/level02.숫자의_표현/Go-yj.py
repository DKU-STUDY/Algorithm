'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12924#
문제 : 숫자의 표현
단순히 중첩 for문을 이용해서 정말로 연속한 자연수의 합이 n과 같은지 확인하는 방법으로 구했다.
그런데 다른 사람들 풀이를 보니 약수중 홀수의 개수로 구하면 된다고 한다.
사실 열심히 읽어보고 이해해보려 했으나 이해가 잘 안됨...
[메모]
len([i for i in range(1,num+1,2) if num%i==0])
'''

def solution(n):
    answer = 0
    num = 0
    for i in range(1,n+1) :
        for j in range(i,n+1) :
            num += j
            if num==n :
                answer += 1
                break
            elif num>n :
                num = 0
                break
    return answer
