from sys import stdin


N = int(stdin.readline())

time_list = list(map(int, stdin.readline().split()))

time_list.sort()

temp = 0
return_value = 0
for idx in range(len(time_list)):
    temp += time_list[idx]
    return_value += temp

print(return_value)