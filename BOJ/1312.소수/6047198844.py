A, B, N = map(int, input().split())
A %= B
for i in range(N - 1):
    A = (A * 10) % B

print((A * 10) // B)