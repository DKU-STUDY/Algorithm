'''
https://programmers.co.kr/learn/courses/30/lessons/12928
약수의 합
[풀이]
1. 제곱근 까지 약수를 구하기. 대칭값까지 더하기. 성능 중심
'''
def solution(n):
    answer = [i for i in range(1, int(n**0.5)+1) if n % i == 0]
    return sum(set(answer + [n // i for i in answer]))
'''
'''