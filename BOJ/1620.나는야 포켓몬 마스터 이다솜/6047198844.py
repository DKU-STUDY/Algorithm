import sys

N, M = map(int, sys.stdin.readline().split())
table = dict()

for i in map(str, range(1, N + 1)):
    pokemon = sys.stdin.readline().rstrip()
    table[pokemon] = i
    table[i] = pokemon

for _ in range(M):
    print(table[sys.stdin.readline().rstrip()])
