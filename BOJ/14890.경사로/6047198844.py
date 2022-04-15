N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


# 이전 블록, 현재 위치, 이전에 두었는지
def func(cy, cx, dy, dx, visited):
    if cy == N or cx == N:
        return True

    # 이전이 없는 경우
    if (cy == 0 and dy == 1) or (cx == 0 and dx == 1):
        return func(cy + dy, cx + dx, dy, dx, visited)

    py, px = cy - dy, cx - dx

    # 이전과 같은 경우
    if arr[py][px] == arr[cy][cx]:
        return func(cy + dy, cx + dx, dy, dx, visited)

    # 이전과 1 이상 차이나는 경우
    if abs(arr[py][px] - arr[cy][cx]) != 1:
        return False

    # 이전이 1 만큼 작은 경우
    if arr[py][px] - arr[cy][cx] == -1:
        for i in range(1, L + 1):
            ny, nx = cy - (i * dy), cx - (i * dx)
            # 이전 칸에 놓을수 있는 경우
            if not (0 <= ny < N and 0 <= nx < N) or arr[py][px] != arr[ny][nx] or (ny, nx) in visited:
                return False
            visited.add((ny,nx))
        # 다음칸
        return func(cy + dy, cx + dx, dy, dx, visited)

    # 이전이 1 만큼 큰 경우
    for i in range(L):
        ny, nx = cy + (i * dy), cx + (i * dx)
        # 현재 칸에 놓을수 있는 경우
        if not (0 <= ny < N and 0 <= nx < N) or arr[cy][cx] != arr[ny][nx] or (ny, nx) in visited:
            return False
        visited.add((ny, nx))
    return func(cy + (dy * L), cx + (dx * L), dy, dx, visited)


res = 0

for y in range(N):
    visited = set()
    res += func(y, 0, 0, +1, visited)

for x in range(N):
    visited = set()
    res += func(0, x, +1, 0, visited)

print(res)
