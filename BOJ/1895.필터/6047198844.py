R, C = map(int, input().split())
pixels = []
res = 0

# 입력
for _ in range(R):
    pixels.append(list(map(int, input().split())))
T = int(input())

# 정제
for y in range(1, R-1):
    for x in range(1, C-1):
        filtered = list()
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                filtered.append(pixels[y+dy][x+dx])
        filtered.sort()
        if filtered[4] >= T:
            res += 1

print(res)