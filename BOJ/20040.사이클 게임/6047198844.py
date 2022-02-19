import sys


def union(A, B):
    PA = find(A)
    PB = find(B)

    if PA == PB:
        return
    P[PB] = PA


def find(A):
    if P[A] == -1:
        return A
    P[A] = find(P[A])
    return P[A]


n, m = map(int, sys.stdin.readline().split())
P = [-1 for _ in range(n)]
for i in range(1, m+1):
    v, w = map(int, sys.stdin.readline().split())
    pv = find(v)
    pw = find(w)

    if pv == pw:
        print(i)
        break
    union(v, w)

else:
    print(0)
