import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, K = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()

    left = 0
    right = len(arr) - 1

    most_near_n = sys.maxsize
    most_near_cnt = 0

    while left < right:
        if abs(K - arr[left] - arr[right]) < abs(K - most_near_n):
            most_near_n = arr[left] + arr[right]
            most_near_cnt = 1
        elif abs(K - arr[left] - arr[right]) == abs(K - most_near_n):
            most_near_cnt += 1

        if arr[left] + arr[right] <= K:
            left += 1
        else:
            right -= 1
    print(most_near_cnt)