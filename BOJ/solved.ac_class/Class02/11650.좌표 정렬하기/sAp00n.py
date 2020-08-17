from sys import stdin

N = int(stdin.readline())

dots = []
temp = {}
for i in range(N):
    dots.append(list(map(int, stdin.readline().split())))

for dot in dots:
    if dot[0] not in temp:
        temp[dot[0]] = []
    if len(temp[dot]) == 1:
        temp[dot[0]].append(dot)
    else:
        idx = 0
        while temp[dot[0]][idx][-1]>