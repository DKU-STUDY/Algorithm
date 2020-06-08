class CountSemiPrimes:
    def __init__(self, N, P, Q):
        self.spacesize = N
        self.P = P
        self.Q = Q
        self.PQ_len = len(P)
        self.semi_prime_list = self.count_semi_prime()
        print(
            f'class inited\n self.N:{self.spacesize}    self.P: {self.P}    self.Q: {self.Q}    self.PQ_len: {self.PQ_len}    self.semi_prime_list: {self.semi_prime_list}')

    def count_prime(self):
        prime_list = [i for i in range(2, int(self.spacesize / 2) + 1)]
        idx = 0
        while idx <= len(prime_list) - 1:
            i = idx + 1
            while i <= len(prime_list) - 1:
                if prime_list[i] % prime_list[idx] == 0:
                    prime_list.pop(i)
                i += 1
            idx += 1
        return prime_list

    def count_semi_prime(self):
        prime_list = self.count_prime()
        length_of_prime_list = len(prime_list)
        semi_prime_list = []
        for i in range(length_of_prime_list):
            j = i
            while prime_list[j] <= self.spacesize / prime_list[i]:
                if prime_list[i] * prime_list[j] <= self.spacesize:
                    semi_prime_list.append(prime_list[i] * prime_list[j])
                j += 1
                if j > length_of_prime_list-1:
                    break
        semi_prime_list.sort()
        return semi_prime_list

    def compute_return_list(self):
        return_list = []
        length_of_semi_prime_list = len(self.semi_prime_list)
        if length_of_semi_prime_list == 0:
            return [0]
        for idx in range(self.PQ_len):
            the_former = 0
            the_latter = length_of_semi_prime_list - 1
            while self.semi_prime_list[the_former] < self.P[idx] and the_former <= length_of_semi_prime_list - 1:
                the_former += 1
            while self.semi_prime_list[the_latter] > self.Q[idx] and the_latter >= 0:
                the_latter -= 1
            the_latter += 1
            print(f'the_former: {the_former}    the_latter: {the_latter}')
            return_list.append(len(self.semi_prime_list[the_former:the_latter]))
        return return_list


def solution(N, P, Q):
    semiprime_prob = CountSemiPrimes(N, P, Q)
    return semiprime_prob.compute_return_list()


print(solution(P=[1, 4, 16], Q=[26, 10, 20], N=26))
