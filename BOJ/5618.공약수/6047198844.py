def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
nums = list(map(int, input().split()))

gcd = gcd(nums[0], nums[1]) if n == 2 else gcd(gcd(nums[0], nums[1]), nums[2])

for i in range(1, gcd + 1):
    if gcd % i == 0:
        print(i)