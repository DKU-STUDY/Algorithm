def solution(M, A):
    appearance = [False] * (M + 1)
    N = len(A)
    front = 0
    slices = 0
    for back in range(N):
        while front < N and appearance[A[front]] == 0:
            appearance[A[front]] += 1
            slices += front - back +1
            front += 1
        appearance[A[back]] -= 1
        if slices >= 1000000000: return 1000000000
    return slices


M = 6
# A = [0]
A = [3, 4, 5, 5, 2]
#A = [1, 0, 1, 1, 0, 0]
print(solution(M, A))
