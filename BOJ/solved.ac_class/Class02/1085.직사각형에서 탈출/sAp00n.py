from sys import stdin
x, y, w, h = map(int, stdin.readline().split())
escape_condition = [(x, 0), (0, y), (x, h), (w, y)]

min_distance = ((x-escape_condition[0][0])**2 + (y-escape_condition[0][1])**2) ** 0.5
for i in range(1, 4):
    min_distance = min(min_distance, ((x-escape_condition[i][0])**2 + (y-escape_condition[i][1])**2) ** 0.5)
print(int(min_distance))