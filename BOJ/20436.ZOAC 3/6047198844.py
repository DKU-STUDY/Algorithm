left_hand = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v'}
right_hand = {'y','u','i','o','p','h','j','k','l','b','n','m'}

table = dict(tuple())
table['q'] = (0, 0)
table['w'] = (0, 1)
table['e'] = (0, 2)
table['r'] = (0, 3)
table['t'] = (0, 4)
table['y'] = (0, 5)
table['u'] = (0, 6)
table['i'] = (0, 7)
table['o'] = (0, 8)
table['p'] = (0, 9)
table['a'] = (1, 0)
table['s'] = (1, 1)
table['d'] = (1, 2)
table['f'] = (1, 3)
table['g'] = (1, 4)
table['h'] = (1, 5)
table['j'] = (1, 6)
table['k'] = (1, 7)
table['l'] = (1, 8)
table['z'] = (2, 0)
table['x'] = (2, 1)
table['c'] = (2, 2)
table['v'] = (2, 3)
table['b'] = (2, 4)
table['n'] = (2, 5)
table['m'] = (2, 6)

l, r = input().split()

res = 0
l_position, r_position = table[l], table[r]

for char in input():
    x1, y1 = table[char]
    if char in left_hand:
        x2, y2 = l_position
        l_position = table[char]
    else:
        x2, y2 = r_position
        r_position = table[char]

    res += 1 + abs(x1-x2) + abs(y1-y2)

print(res)