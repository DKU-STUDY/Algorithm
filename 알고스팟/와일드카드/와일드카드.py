from sys import stdin


def match(w_idx, s_idx):
    global w
    global s
    global memo
    w_start_idx = w_idx
    s_start_idx = s_idx
    # print(f'input_list -> {w[w_start_idx:]} matching : {s[s_start_idx:]}')

    if (w_start_idx, s_start_idx) in memo:
        # print(f'in memo\nreturn_value ->{memo[(w_start_idx, s_start_idx)]}')
        return memo[(w_start_idx, s_start_idx)]
    idx = 0
    # print(f'start_matching at {idx} < {len(w[w_start_idx:]) - 1} or {idx} < {len(s[s_start_idx:]) - 1}')
    while idx < len(w[w_start_idx:]) and idx < len(s[s_start_idx:]):
        if w[w_start_idx + idx] == s[s_start_idx + idx] or w[w_start_idx + idx] == '?':
            idx += 1
            # print(f'    list: {w[w_start_idx + idx:]} matching: {s[s_start_idx + idx:]}')
            continue
        break

    if w_start_idx + idx == len(w) and s_start_idx + idx == len(s):
        memo[(w_start_idx, s_start_idx)] = True
        # print(f'        case {w[w_start_idx + idx:]} -> {s[s_start_idx + idx:]} is True')
        return True

    if len(w[w_start_idx + idx:]) >= 1 and w[w_start_idx + idx] == '*':
        # print(f'fst letter is "*"')
        for jdx in range(0, len(s[s_start_idx:]) - idx + 1):
            # print(f'match( {w[w_start_idx + idx + 1:]} , {s[s_start_idx + idx + jdx:]} ) ')
            if match(w_start_idx + idx + 1, s_start_idx + idx + jdx):
                memo[(w_start_idx + idx + 1, s_start_idx + idx + jdx)] = True
                return True
    memo[(w_start_idx, s_start_idx)] = False
    return False


def sol():
    global w
    global s
    global memo
    w = stdin.readline().strip('\n')
    n = int(stdin.readline())
    return_li = []
    for __ in range(n):
        s = stdin.readline().strip('\n')
        memo = {}
        if match(0, 0):
            return_li.append(s)
        # print(f'memo: {memo}\n\n')
    return_li.sort()
    for li in return_li:
        print(li)

C = int(stdin.readline())
for _ in range(C):
    sol()
