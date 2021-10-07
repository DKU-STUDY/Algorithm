N, M = map(int, input().split())
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