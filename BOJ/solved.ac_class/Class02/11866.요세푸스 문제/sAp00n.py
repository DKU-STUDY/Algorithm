from sys import stdin
from collections import deque

N, K = list(map(int, stdin.readline().split()))
jump = K-1
circle = deque()
return_str = '<'
for i in range(1, N+1):
    circle.append(i)

for j in range(N):
    circle.rotate(-jump)
    return_str += (str(circle.popleft())+', ')
return_str = return_str[:-2]
return_str += '>'
print(return_str)


