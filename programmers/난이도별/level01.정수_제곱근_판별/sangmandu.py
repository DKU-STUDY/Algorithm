'''
https://programmers.co.kr/learn/courses/30/lessons/12934
정수 제곱근 판별
[풀이]
1. ** 사용
'''
def solution(n):
    return (n ** 0.5 + 1) ** 2 if int(n ** 0.5) ** 2 == n else -1
'''
참고로 math.is_integer()를 사용할 수도 있음
'''