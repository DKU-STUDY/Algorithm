table = dict()
table['A'] = 3
table['B'] = 2
table['C'] = 1
table['D'] = 2
table['E'] = 3
table['F'] = 3
table['G'] = 3
table['H'] = 3
table['I'] = 1
table['J'] = 1
table['K'] = 3
table['L'] = 1
table['M'] = 3
table['N'] = 3
table['O'] = 1
table['P'] = 2
table['Q'] = 2
table['R'] = 2
table['S'] = 1
table['T'] = 2
table['U'] = 1
table['V'] = 1
table['W'] = 2
table['X'] = 2
table['Y'] = 2
table['Z'] = 1

nums = list(map(lambda char: table[char], list(input())))

while len(nums) > 1:
    tmp = list()
    for idx in range(1, len(nums), 2):
        tmp.append(nums[idx-1] + nums[idx])
    if len(nums) % 2 == 1:
        tmp.append(nums[len(nums)-1])
    nums = tmp
print("I'm a winner!") if nums[0] % 2 == 1 else print("You're the winner?")