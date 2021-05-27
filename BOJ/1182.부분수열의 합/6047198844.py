from itertools import combinations

#idx를 뽑거나 뽑지 않는 경우의수.
#N개를 뽑았을때 합이 S면 True, 아니면 False반환
#idx 현재 판단의 기준이되는 idx / 목표하는 합 S / 누적합 partial_sum
def partial_sequence(idx:int, N:int, S:int, partial_sum:int, sequence:list):
    if N < 0:
        return 0
    
    if idx == len(sequence):
        if partial_sum == S and N == 0:
            return 1
        return 0

    res = 0
    res += partial_sequence(idx+1, N-1, S, partial_sum+sequence[idx], sequence)
    res += partial_sequence(idx+1, N, S, partial_sum, sequence)
    return res

N, S = map(int, input().split())
sequence = list(map(int, input().split()))

res = 0
for _ in range(1,N+1):
    res += partial_sequence(0, _, S, 0, sequence)
print(res)