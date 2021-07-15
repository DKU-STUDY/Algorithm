'''
https://programmers.co.kr/learn/courses/30/lessons/12910
나누어 떨어지는 숫자 배열
[풀이]
0. 나머지가 0 인 수 찾기
1. divmod 사용
'''
def solution(arr, divisor):
    answer = [i for i in sorted(arr) if divmod(i, divisor)[1] == 0]
    return answer if len(answer) != 0 else [-1]
'''
배울 점이 있는 코드
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
len == 0 을 비교할 때는 if else 대신 False or True 를 이용할 수 있음
'''