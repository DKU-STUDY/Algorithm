N = int(input())
A, B = 2, 4
for _ in range(N - 1):
    A, B = B, A + B
print(B)

# 4, 6, 10, 16, 26