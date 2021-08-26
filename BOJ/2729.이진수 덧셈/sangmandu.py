'''
https://www.acmicpc.net/problem/2729
이진수 덧셈
[풀이]
1. int(x, 2)는 이진수를 십진수로 변환
2. format(num, 'b')는 num을 이진수(=binary)로 변환
'''
import sys
input = sys.stdin.readline
N = int(input().strip())
for _ in range(N):
    a, b = map(lambda x : int(x, 2), input().strip().split())
    print(format(a+b, 'b'))