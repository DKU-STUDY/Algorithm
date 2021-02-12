'''
https://programmers.co.kr/learn/courses/30/lessons/12945
피보나치 수
'''

def solution(n):
    fibonachi = [0, 1]
    for i in range(2, n+1):
        fibonachi.append(fibonachi[i-1] + fibonachi[i-2])
    return fibonachi[-1] % 1234567

'''
메모리를 적게 쓰는 방법.
당연히 속도가 빨라지면 메모리는 많이 쓰게 되는 tradeoff로 생각했는데,
속도와 메모리를 둘 다 잡은 코드.
a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a
'''