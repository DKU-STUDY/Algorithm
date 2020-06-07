import time
start = time.time()

def solution(N):
    number_of_factors = 0
    i = 1
    while i*i < N:
        if N % i == 0:
            number_of_factors += 2
        i += 1
    if i * i == N:
        number_of_factors += 1
    return number_of_factors

print(solution(1))
print(f'time = {time.time()-start}')