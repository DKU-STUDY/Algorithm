from sys import stdin
a = list(map(int, stdin.readline().split()))

if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')
