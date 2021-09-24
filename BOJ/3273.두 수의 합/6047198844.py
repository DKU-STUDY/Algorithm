n = int(input())
LIST = list(map(int, input().split()))
LIST.sort()
x = int(input())
begin, end = 0, len(LIST) - 1
res = 0
while begin < end:
    m1, m2 = LIST[begin], LIST[end]
    sum = m1 + m2
    if sum < x:
        begin += 1
    elif sum > x:
        end -= 1
    else:
        while m1 == LIST[begin]:
            begin += 1
            res += 1
        while m2 == LIST[end]:
            end -= 1
            res += 1
        res -= 1
print(res)