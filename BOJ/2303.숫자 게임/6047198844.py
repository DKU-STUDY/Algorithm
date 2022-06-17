from itertools import combinations

N = int(input())
res_person = 1
res_num = 0

for i in range(1, N+1):
    for j in combinations(map(int, input().split()), 3):
        s = sum(j)
        if s % 10 >= res_num:
            res_num = s % 10
            res_person = i
print(res_person)