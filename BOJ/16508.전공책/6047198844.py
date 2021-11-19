from itertools import combinations

T = list(input())
N = int(input())
books = list()
for _ in range(N):
    money, book = input().split()
    books.append((int(money), list(book)))

res = 9999999999999
for i in range(1, N+1):
    for pick_books in combinations(books, i):
        target = T.copy()
        acc = 0
        for pick_book in pick_books:
            money, book = pick_book
            is_cut = False
            for word in book:
                if word in target:
                    is_cut = True
                    target.remove(word)
            if is_cut:
                acc += money
        if not target:
            res = min(res, acc)

if res == 9999999999999:
    res = -1
print(res)






res = 0
# for book in books:
#     money, book = book
#     is_cut = False
#     for word in book:
#         if word in T:
#             is_cut = True
#             T.remove(word)
#     if is_cut:
#         res += money
#
# if T:
#     print(res)
# else:
#     print(-1)