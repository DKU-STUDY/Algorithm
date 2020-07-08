def solution(P, Q, N):
    max_num = N
    prime_list = sieve(max_num)
    print(prime_list)

    for i in range(max_num):
        start_num = find_startidx_in_logNtime(prime_list, i)
        print(f'시작숫자:  {i}     구간 시작: {start_num}')

    """for idx in range(len(P)):
        start_num = find_startidx_in_logNtime(prime_list, P[idx])
        print(f'시작숫자:  {P[idx]}     구간 시작: {start_num}')"""



def find_startidx_in_logNtime(prime_list, Num):
    # 가능한 가장 큰 소수보다 시작 숫자가 큰 경우 => 예외 처리
    if Num > prime_list[-1]:
        return False
    # 가능한 가장 작은 소수보다 시작 숫자가 같거나 작은 경우 => 가장 작은 소수부터 시작
    if Num <= prime_list[0]:
        return prime_list[0]

    N = len(prime_list)
    n = int(N/2)

    while not (prime_list[n - 1] < Num <= prime_list[n]):
        print(f'n: {n}    {prime_list[n-1]} < {Num} <= {prime_list[n]}')
        if prime_list[n] < Num:
            if ((N-n)/2) < 1:
                n += 1
                continue
            else:
                n = n + int((N-n)/2)
                continue

        if Num <= prime_list[n-1]:
            if (n/2) < 1:
                n -= 1
            else:
                n = int(n/2)

        if prime_list[n-1] < Num and prime_list[n] < Num:
            print('2')
            if ((n*2)-n)/2 < 1:
                n += 1
            else:
                n = n+int(((n*2)-n)/2)

    return prime_list[n]




def sieve(max_num):
    prime_list = []
    prime_dic = {}
    for i in range(2, max_num + 1): prime_dic[i] = [True]
    for i in range(2, max_num + 1):
        if prime_dic[i] == False:
            continue
        common = i * 2
        while common < max_num+1:
            prime_dic[common] = False
            common += i

    for i in range(2, max_num + 1):
        if prime_dic[i]:
            prime_list.append(i)
    return prime_list


print(solution(P=[1, 4, 16], Q=[26, 10, 20], N=26))
