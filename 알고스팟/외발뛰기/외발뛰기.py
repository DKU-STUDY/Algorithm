from sys import stdin


def recursive_jump(mat, location):
    # print(f'cache : {cache}')
    if mat[location[0]][location[1]] == 0:
        return True
    if location in cache:
        return cache[location]
    current_num = mat[location[0]][location[1]]
    case_01, case_02 = False, False
    if location[0] + current_num <= len(mat) - 1:
        case_01 = recursive_jump(mat, (location[0] + current_num, location[1]))
        cache[(location[0] + current_num, location[1])] = case_01
    if location[1] + current_num <= len(mat) - 1:
        case_02 = recursive_jump(mat, (location[0], location[1] + current_num))
        cache[location[0], location[1] + current_num] = case_02
    if case_01 or case_02:
        return True
    else:
        return False


def sol():
    n = int(stdin.readline())
    mat = [list(map(int, stdin.readline().split())) for _ in range(n)]
    '''for line in mat:
        print(line)'''

    if recursive_jump(mat, (0, 0)):
        print('YES')
    else:
        print('NO')


C = int(stdin.readline())

for _ in range(C):
    cache = {}
    sol()
