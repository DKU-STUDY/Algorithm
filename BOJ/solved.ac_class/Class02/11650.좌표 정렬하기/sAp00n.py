from sys import stdin
N = int(stdin.readline())
dots = [] * range(N)
for i in range(N):
    dots[i] = list(map(int,stdin.readline().split()))

dots.sort()
for i in dots:
    print(f'{i[0]} {i[1]}')
