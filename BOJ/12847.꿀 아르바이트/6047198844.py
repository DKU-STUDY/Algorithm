n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = sum(arr[0:m])
res = start
for i in range(n-m):
    start = start - arr[i] + arr[i+m]
    res = max(res, start)
print(res)