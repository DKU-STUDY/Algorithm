from random import randint

import time


def logging_time(original_fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = original_fn(*args, **kwargs)
        end_time = time.time()
        print(f"WorkingTime[{original_fn.__name__}]: {end_time - start_time} sec")
        return result

    return wrapper_fn


@logging_time
def solution(N):
    # write your code in Python 3.6
    bin_n = str(bin(N)[2:])
    print(f'bin_N = {bin_n}')
    ans = 0
    current = 0
    last = 0
    while True:
        current = bin_n.find('1', last + 1)
        # print(f'temp = {temp}')
        if current == -1:
            return -1 if last == 0 else ans
        if current - (last + 1) > ans:
            ans = current - (last + 1)
        last = current


N = randint(1, 2147483647)
print(f'input decaN= {N}')

print(solution(N))