import collections


N = int(input())
r1, c1, r2, c2 = map(int, input().split())
Q = collections.deque()
discovered = set()
Q.append((r1,c1))
discovered.add((r1,c1))

move_cnt = 0
while Q:
    move_cnt += 1
    for _ in range(len(Q)):
        r, c = Q.popleft()
        for dr, dc in (-2, -1), (-2, +1), (0, -2), (0, +2), (+2, -1), (+2, +1):
            nr = r + dr
            nc = c + dc

            #범위를 벗어난 경우
            if not (0 <= nr <N and 0 <= nc < N):
                continue

            #목적지에 도달한 경우
            if nr == r2 and nc == c2:
                print(move_cnt)
                exit()

            if (nr, nc) not in discovered:
                Q.append((nr, nc))
                discovered.add((nr, nc))

print(-1)