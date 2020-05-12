from random import randint


def solution(N):
    # write your code in Python 3.6
    bin_n = bin(N)
    # print(f'bin_N = {bin_n}')
    ans = 0
    temp = -1
    condition = None
    for i in bin_n[2:]:
        # print(i)
        if i == '1':
            if condition is None:
                # print('check')
                condition = True
            elif condition is True:
                if temp > ans:
                    ans = temp
                temp = -1
        if condition:
            temp += 1
    return ans


N = randint(1, 2147483647)
print(f'input decaN= {N}')

print(solution(N))
