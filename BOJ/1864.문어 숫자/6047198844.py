octopus = dict()
octopus['-'] = 0
octopus["\\"] = 1
octopus['('] = 2
octopus['@'] = 3
octopus['?'] = 4
octopus['>'] = 5
octopus['&'] = 6
octopus['%'] = 7
octopus['/'] = -1

while True:
    octopus_num = input()[::-1]
    if octopus_num == '#':
        break
    res = 0
    for idx, n in enumerate(octopus_num):
        res += int(octopus[n]) * (8 ** int(idx))
    print(res)