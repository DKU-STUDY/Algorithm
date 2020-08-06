def check_BW(ex):
    cnt1 = 0
    for i in range(8):
        for j in range(8):
            i_ = (0 if i in [0, 2, 4, 6] else 1)
            j_ = (0 if j in [0, 2, 4, 6] else 1)
            if (i_ == 0 and j_ == 0) or (i_ == 1 and j_ == 1):
                if ex[i][j] != "B": cnt1 += 1
            if (i_ == 0 and j_ == 1) or (i_ == 1 and j_ == 0):
                if ex[i][j] != "W": cnt1 += 1

    cnt2 = 0
    for i in range(8):
        for j in range(8):
            i_ = (0 if i in [0, 2, 4, 6] else 1)
            j_ = (0 if j in [0, 2, 4, 6] else 1)
            if (i_ == 0 and j_ == 0) or (i_ == 1 and j_ == 1):
                if ex[i][j] != "W": cnt2 += 1
            if (i_ == 0 and j_ == 1) or (i_ == 1 and j_ == 0):
                if ex[i][j] != "B": cnt2 += 1

    return min(cnt1, cnt2)


n, m = map(int, input().split())
s = [list(input()) for i in range(n)]
check = list()
for i in range(n - 7):
    for j in range(m - 7):
        ex = [z[(0 + j):(8 + j)] for z in s[(0 + i):(8 + i)]]
        check.append(check_BW(ex))
print(min(check)
