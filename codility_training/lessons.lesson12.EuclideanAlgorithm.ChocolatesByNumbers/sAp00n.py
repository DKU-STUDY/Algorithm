def solution(N, M):
    def gcd(N, M):
        if N % M == 0:
            return M
        else:

            return gcd(M, N % M)

    return N // gcd(N, M)


print(solution(10, 4))
