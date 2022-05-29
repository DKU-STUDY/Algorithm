import sys

i = 0
while True:
    i += 1
    L, P, V = map(int, sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0:
        break
    print('Case {}: {}'.format(i, (V // P) * L + min(V % P, L)))
