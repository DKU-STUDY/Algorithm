X, Y = map(int, input().split())
target = 100 * Y // X

# 판수 범위.
begin = 1
end = 1000000000 + 1

# lower_bound
while begin < end:
    mid = (begin + end) // 2
    win_rate = 100 * (Y + mid) // (X + mid)

    if win_rate <= target:
        begin = mid + 1
    else:
        end = mid

if target == 100 * (Y + begin) // (X + begin):
    print(-1)
else:
    print(begin)

# float을 int()형변환하는건 위험하다.
