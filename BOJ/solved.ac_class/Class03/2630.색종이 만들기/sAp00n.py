from sys import stdin


def recursion(mat,return_list):
    blue_count = 0
    white_count = 0
    for rows in mat:
        for ele in rows:
            if ele == 1:
                blue_count += 1
            else:
                white_count += 1
    if blue_count == 0 or white_count == 0:
        return_list.append(mat)
        return
    else:
        sliced_mat = slicer(mat)
        return recursion(sliced_mat[0],return_list), recursion(sliced_mat[1],return_list), recursion(sliced_mat[2],return_list), recursion(sliced_mat[3],return_list)


def slicer(mat):
    len_of_mat = len(mat)
    half_len = len_of_mat // 2
    return_list = [[], [], [], []]
    for i in range(len_of_mat):
        if i < half_len:
            return_list[0].append(mat[i][:half_len])
            return_list[1].append(mat[i][half_len:])
        else:
            return_list[2].append(mat[i][:half_len])
            return_list[3].append(mat[i][half_len:])
    return return_list


N = int(stdin.readline())

mat = [list(map(int, stdin.readline().split())) for i in range(N)]

result = []
recursion(mat,result)
#print(result)

b_count = 0
w_count = 0

for sliced in result:
    if sliced[0][0] == 1:
        b_count += 1
    else:
        w_count += 1

print(f'{w_count}\n{b_count}')
