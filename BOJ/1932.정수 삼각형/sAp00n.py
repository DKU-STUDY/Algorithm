from sys import stdin


triang_list = [tuple(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))]
DP = [[] for _ in range(len(triang_list))]
DP[0].append(triang_list[0][0])
for num_of_line in range(1, len(triang_list)):
    for idx in range(len(triang_list[num_of_line])):
        compare_list = []
        if idx == 0:
            compare_list.append(DP[num_of_line - 1][0])
        elif idx == len(triang_list[num_of_line]) - 1:
            compare_list.append(DP[num_of_line - 1][-1])
        else:
            compare_list += [DP[num_of_line - 1][idx - 1], DP[num_of_line - 1][idx]]

        DP[num_of_line].append(max(compare_list) + triang_list[num_of_line][idx])
print(max(DP[-1]))
