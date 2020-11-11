from sys import stdin

N = int(stdin.readline())

meeting_list = []

for idx in range(N):
    meeting_list.append(list(map(int, stdin.readline().split())))

meeting_list = sorted(meeting_list, key=lambda x: (x[1], x[0]))

count = 0
last = 0
for meet in meeting_list:
    if last <= meet[0]:
        count += 1
        last = meet[1]
print(count)
