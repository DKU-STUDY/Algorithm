# 1, 3, 5, 7, 9, 7, 3, 1
N = int(input())
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * ((i - 1) * 2 + 1))
for i in range(1, N + 1):
    print(' ' * i + '*' * ((N - i - 1) * 2 + 1))
