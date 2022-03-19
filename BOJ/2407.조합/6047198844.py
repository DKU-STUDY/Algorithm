n, m = map(int, input().split())

res = 1
for i in range(m):
    res *= (n-i)
for i in range(1, m+1):
    res //= i
print(res)