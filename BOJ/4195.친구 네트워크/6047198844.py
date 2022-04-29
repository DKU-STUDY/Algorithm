import sys


def union(A, B):
    PA = find(A)
    PB = find(B)

    if PA != PB:
        P[PB] = PA
        N[PA] += N[PB]
    return N[PA]




def find(A):
    if P[A] == A:
        return P[A]
    P[A] = find(P[A])
    return P[A]


T = int(sys.stdin.readline())
for _ in range(T):
    F = int(sys.stdin.readline())
    P = {}
    N = {}

    for _ in range(F):
        A, B = sys.stdin.readline().split()
        if A not in P:
            P[A] = A
            N[A] = 1
        if B not in P:
            P[B] = B
            N[B] = 1
        print(union(A, B))
