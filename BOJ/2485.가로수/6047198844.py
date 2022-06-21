def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


N = int(input())
arr = list(sorted([int(input()) for _ in range(N)]))
intervals = list(set([arr[i] - arr[i - 1] for i in range(1, N)]))

if len(intervals) >= 2:
    gcd_num = gcd(intervals[0], intervals[1])
    for i in range(2, len(intervals)):
        gcd_num = gcd(gcd_num, intervals[i])
else:
    gcd_num = intervals[0]

start = arr[0]
end = arr[-1]
min_cnt = (end - start) // gcd_num
print(min_cnt - N + 1)