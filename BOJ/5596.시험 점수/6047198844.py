result = -1
for _ in range(2):
    arr = list(map(int, input().split()))
    result = max(result, sum(arr))
print(result)