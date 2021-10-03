from collections import Counter

N = int(input())
books = list()
for _ in range(N):
    books.append(input())

books = Counter(books)
books = sorted(books, key=lambda x: (-books.get(x), x))
print(books[0])