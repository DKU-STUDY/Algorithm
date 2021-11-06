a, b = map(int, input().split())
b = min(10000000, b)
# 소수이면 True
is_prime = [True] * (int(b ** 0.5) + 1)
divisors = []

# 정답의 범위는 a ~ 최대 10000000 이다.
# 이들의 약수중 하나는 반드시 10000000 ** 0.5의 범위안에 들어온다.
for i in range(2, int(b ** 0.5) + 1):
    if is_prime[i]:
        divisors.append(i)
        for j in range(i + i, int(b ** 0.5) + 1, i):
            is_prime[j] = False

# 짝수는 고려하지 않는다.
if a % 2 == 0:
    a += 1

for i in range(a, b + 1, 2):
    # 팰린드롬인가? 크기가 홀수 또는 11인가?
    if (i == 11 or len(str(i)) % 2 == 1) and str(i) == str(i)[::-1]:
        for divisor in divisors:
            if divisor < i and i % divisor == 0:
                break
        else:
            print(i)

print(-1)