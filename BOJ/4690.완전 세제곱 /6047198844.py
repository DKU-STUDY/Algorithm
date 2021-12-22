from itertools import combinations

res = []
for b, c, d in combinations(range(1,101),3):
    a = (b ** 2 + c ** 2 + d ** 2) ** (0.5)
    if 100 >= a == int(a):
        res.append((int(a), b, c, d))

res.sort()
for a, b, c, d in res:
    print(f'Cube = {a}, Triple = ({b},{c},{d})')