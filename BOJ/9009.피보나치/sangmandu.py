'''
https://www.acmicpc.net/problem/9009
피보나치
[풀이]
1. 이 문제의 핵심 다음과 같다
1.1 모든 양의 정수는 하나 이상의 서로 다른 피보나치 수들의 합으로 나타낼 수 있다
=> 문제에 제시된 조건이며 https://ko.wikiqube.net/wiki/Complete_sequence 에서 확인 가능하다
1.2 어떤수를 피보나치 수들로 표현할 때 가장 큰 피보나치를 사용하는 것이 적은 수의 피보나치를 사용할 수 있다는 것이다.
=> 왜일까?
2. 이 부분은 다음을 증명해야 한다.
2-1. 유일성
=> 두개의 연속한 피보나치 수를 포함하지 않는 유일한 표현 방법이 존재한다
=> https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem 에서 증명
2-2. 유일한 표현 방법이 최소이다
=> 만약에 연속한 피보나치 수를 포함하는 방법이 최소라고 가정하자
=> 그러면 연속한 피보나치 수는 또다른 피보나치수로 만들 수 있다
=> 따라서 최소라고 정의한 가정에 모순이므로 유일한 표현 방법이 최소이다
'''
n = int(input())
for i in range(n):
    m = int(input())
    fibo = [0, 1]
    idx = 0
    while fibo[idx]+fibo[idx+1] <= m:
        fibo.append(fibo[idx]+fibo[idx+1])
        idx += 1

    total = m
    answer = []
    for f in fibo[:0:-1]:
        if total >= f:
            total -= f
            answer.append(f)

    print(*answer[::-1])
