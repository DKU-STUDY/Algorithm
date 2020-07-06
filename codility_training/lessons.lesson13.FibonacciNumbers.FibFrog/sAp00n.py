def solution(A):
    A = [1] + A + [1]
    print(A)
    length_of_A = len(A)
    leap_location = []
    for i in range(length_of_A):
        if A[i] != 0:
            leap_location.append(i)
    print(f'leap_location : {leap_location}')

    last = 0
    current = 1
    fibo_list = []
    while current < length_of_A:
        fibo_list.append(current + last)
        temp = last
        last = current
        current = temp + current

    #print(fibo_list)

    head_location = 0
    jump_num = 0
    jump_num = frog_jumping(A, fibo_list, head_location, jump_num)
    jump_num = jump_num[0]

    return jump_num


def frog_jumping(A, fibo_list, head, jump_num):
    for idx in range(len(A)-1, head, -1):
        if (idx in fibo_list) and (A[idx] == 1):
            print(f'head:{head} idx:{idx} A[idx]:{A[idx]}')
            head = idx
            jump_num += 1
            if head == len(A)-1:
                return jump_num, True
            temp = A[idx]
            A_02 = A[idx:]
            head_02 = 0
            cache = frog_jumping(A_02, fibo_list, head_02, jump_num)
            if cache[1] == True:
                return cache
    return -1, False


'''A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
print(solution(A))
B = [0, 0, 0]
print(solution(B))'''
C = [1,1,0,0,0]
print(solution(C))
