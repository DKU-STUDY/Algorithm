N, M = map(int, input().split())
if N != 0:
    books = map(int, input().split())
    ans = 1
    cur_weight = 0
    for book in books:
        if cur_weight + book <= M:
            cur_weight += book
        else:
            cur_weight = book
            ans += 1
    print(ans)
else:
    print(0)