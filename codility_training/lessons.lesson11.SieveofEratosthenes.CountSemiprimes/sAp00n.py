def solution(N, P, Q):
    from math import sqrt
    prime_table = [False]*2+[True]*(N-1)
    prime = []
    prime_count = 0
    for element in range(2, int(sqrt(N))+1):
        if prime_table[element] == True:
            prime.append(element)
            prime_count += 1
            multiple = element * element
            while multiple <= N:
                prime_table[multiple] = False
                multiple += element
    for element in range(int(sqrt(N))+1, N+1):
        if prime_table[element] == True:
            prime.append(element)
            prime_count += 1
    semiprime = [0] * (N+1)
    for index_former in range(prime_count-1):
        for index_latter in range(index_former, prime_count):
            if prime[index_former]*prime[index_latter] > N:
                break
            semiprime[prime[index_former]*prime[index_latter]] = 1
    for index in range(1, N+1):
        semiprime[index] += semiprime[index-1]
    question_len = len(P)
    result = [0]*question_len
    for index in range(question_len):
        result[index] = semiprime[Q[index]] - semiprime[P[index]-1]
    return result


print(solution(P=[1, 4, 16], Q=[26, 10, 20], N=26))
