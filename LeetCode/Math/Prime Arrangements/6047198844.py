class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # 소수 2개. 일반수 3개 2! * 3!
        #
        prime = [True for _ in range(n + 1)]
        prime[0] = False
        prime[1] = False

        for i in range(1, n + 1):
            if prime[i]:
                for j in range(i + i, n + 1, i):
                    prime[j] = False
        cnt = math.factorial(prime.count(True)) * math.factorial(prime.count(False) - 1)
        return (cnt % (10 ** 9 + 7))