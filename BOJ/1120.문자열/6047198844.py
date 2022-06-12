import math

A, B = input().split()

res = math.inf
for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            cnt += 1
    res = min(cnt, res)
print(res)