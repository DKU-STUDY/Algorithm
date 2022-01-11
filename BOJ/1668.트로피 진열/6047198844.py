import sys

N = int(sys.stdin.readline().rstrip())

left, right = 0, 0
left_res, right_res = 0, 0

trophies = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
for trophy in trophies:
    if left < trophy:
        left = trophy
        left_res += 1

for trophy in trophies[::-1]:
    if right < trophy:
        right = trophy
        right_res += 1
print(left_res)
print(right_res)
