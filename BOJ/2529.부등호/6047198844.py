from itertools import permutations

N = int(input())
sign = input().split()
number = list(map(int, range(10)))
res = []

for i in permutations(number, N+1):
    flag = True
    for idx in range(1,N+1):
        if sign[idx-1] == '<' and i[idx-1] > i[idx]:
            flag = False
            break

        if sign[idx-1] == '>' and i[idx-1] < i[idx]:
            flag = False
            break
    if flag:
        res.append(i)

for _ in res[-1]:
    print(_, end='')

print()

for _ in res[0]:
    print(_, end='')