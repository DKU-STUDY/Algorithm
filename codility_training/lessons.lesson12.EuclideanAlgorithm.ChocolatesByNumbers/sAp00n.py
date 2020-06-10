def solution(N, M):
    choco_list = [True for i in range(N) ]
    idx = 0
    return_val = 0
    if N == 0:
        return 0
    else:
        while choco_list[idx] != False:
            print(f'idx: {idx}  ele : {choco_list[idx]}')
            choco_list[idx] = False
            idx += M
            if idx >= N:
                idx %= N
            return_val += 1
        return return_val


print(solution(947853, 4453))
