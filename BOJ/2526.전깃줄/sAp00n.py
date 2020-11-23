from sys import stdin


list_of_lines = sorted([tuple(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))])
vector = [0] * len(list_of_lines)
vector[0] = 1
for i in range(1, len(list_of_lines)):
    min_value = 0
    for j in range(i):
        if list_of_lines[i][-1] > list_of_lines[j][-1]: min_value = max(vector[j], min_value)
    vector[i] = min_value + 1
print(len(list_of_lines) - max(vector))
