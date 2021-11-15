from itertools import combinations_with_replacement

n = int(input())
squares = [i ** 2 for i in range(225)]
for combinations in combinations_with_replacement(squares, 3):
    if sum(combinations) == n:
        print(len(combinations) - combinations.count(0))
        exit()
print(4)
