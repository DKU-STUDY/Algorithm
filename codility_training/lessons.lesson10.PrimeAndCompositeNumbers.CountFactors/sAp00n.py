def solution(N):
    number_of_factors = 0
    for i in range(1, N+1):
        if N % i == 0:
            print(i)
            number_of_factors += 1
    return number_of_factors
