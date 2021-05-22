from sys import stdin


def recursion_fractal(s, N, K, last_result):
    # base case 01
    if last_result == 0:
        plane = [[0] * N for _ in range(N)]
        mid_idx = N // 2
        mid_idx -= K // 2
        for j in range(K):
            plane[mid_idx + j][mid_idx:mid_idx + K] = [1] * K

    # base case 02
    elif last_result == 1:
        plane = [[1] * N for _ in range(N)]

    if s == 1:
        return plane

    return_plane = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            return_plane[j] = recursion_fractal(s - 1, N, K, plane[i][j])
            print(return_plane)
    return plane


# [C1,R1] ~ [C2,R2]

s, N, K, R_1, R_2, C_1, C_2 = map(int, stdin.readline().split())
fractal_plane = [0] * pow(N, s)
return_mat = recursion_fractal(s, N, K, 0)
for row in return_mat:
    print(row)
