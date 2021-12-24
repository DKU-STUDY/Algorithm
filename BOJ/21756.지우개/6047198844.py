N = int(input())
arr = list(range(1, N + 1))

while len(arr) > 1:
    for idx in range(0, len(arr) // 2 + len(arr) % 2):
        del arr[idx]
print(arr[0])