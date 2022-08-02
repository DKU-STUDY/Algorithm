import sys

min_num, max_num = map(int, sys.stdin.readline().split())
squared_range = max_num - min_num + 1
sieve = [False] * squared_range

i = 2
while i ** 2 <= max_num:
    # 최소 root num 을 찾는다.
    root_num = min_num // (i ** 2)
    if min_num % (i ** 2) != 0:
        root_num += 1

    # root num 을 증가시키면서 체로 거른다.
    while root_num * (i ** 2) <= max_num:
        if not sieve[root_num * (i ** 2) - min_num]:
            sieve[root_num * (i ** 2) - min_num] = True
            squared_range -= 1
        root_num += 1
    i += 1
print(squared_range)
