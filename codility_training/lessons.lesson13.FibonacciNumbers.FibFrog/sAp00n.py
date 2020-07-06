def solution(A):
    A.append(1)
    N = len(A)
    fib = [0] * 27
    fib[1] = 1
    for i in range(2, 27):
        fib[i] = fib[i - 1] + fib[i - 2]
        if fib[i] > N:
            fib = fib[2:i]
            break

    reachable = [-1] * N
    for jump in fib:
        if A[jump - 1] == 1: reachable[jump - 1] = 1

    for i in range(N):
        if A[i] == 1 and reachable[i] < 0:
            min = N + 1
            minidx = -1
            for jump in fib:
                pre = i - jump
                if pre < 0 or reachable[pre] < 0:
                    continue
                if min > reachable[pre]:
                    min = reachable[pre]
                    minidx = pre
            if minidx != -1:
                reachable[i] = min + 1

    return reachable[-1]



A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
print(solution(A))
"""B = [0, 0, 0]
print(solution(B))
C = [1,1,0,0,0]
print(solution(C))"""
