import sys


def union(A, B):
    PA = find(A)
    PB = find(B)

    if PA == PB:
        return
    P[PB] = PA



def find(A):
    if P[A] == A:
        return A
    P[A] = find(P[A])
    return P[A]


gate_num = int(sys.stdin.readline())
airplane_num = int(sys.stdin.readline())
airplanes = [int(sys.stdin.readline()) for _ in range(airplane_num)]

P = [i for i in range(gate_num + 1)]

res = 0
for airplane in airplanes:
    P_airplane = find(airplane)
    if P_airplane == 0:
        break
    union(P_airplane - 1, P_airplane)
    res += 1

print(res)
