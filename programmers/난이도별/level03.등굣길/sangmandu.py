'''
https://programmers.co.kr/learn/courses/30/lessons/42898
등굣길
stack 사용
'''

def solution(m, n, puddles):
    b = [[0] * (m + 1) for _ in range(n + 1)]

    for x, y in puddles:
        if x <= m and y <= n:
            b[y][x] = -1

    b[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if b[i][j] == -1:
                b[i][j] = 0
                continue
            b[i][j] += (b[i - 1][j] + b[i][j - 1])

    return b[n][m] % 1000000007

'''
완전 별로인 문제, 당연히 위아래도 고려해야 하는 줄 알았다.
아래, 왼쪽으로만 진행할 수 있도록 비가 내리는 줄 알았으면 이렇게 고민 안했을 듯

def solution(m, n, puddles):
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack = [([(1, 0)], 1, 1, 0)]
    answer = []

    while stack:
        prior, x, y, dist = stack.pop(0)
        if x == m and y == n:
            answer.append(dist)
            continue
        for a, b in move:
            nx = x + a
            ny = y + b
            if nx <= 0 or nx > m or ny <= 0 or ny > n:
                continue
            for _x, _y in prior:
                if _x == nx and _y == ny:
                    break
            else:
                for _x, _y in puddles:
                    if _x == nx and _y == ny:
                        break
                else:
                    prior.append((x, y))
                    stack.append((prior, nx, ny, dist+1))
    
    return len(answer) % 1000000007
    
위 아래로 갈 수 있다는 전제를 두고 풀은 코드.
잘 풀은건 아니라 이렇게 풀어도 효율이 너무 안좋아서 걸릴 가능성은 높음.
말이 안되는 문제긴 했음. 지나온 길을 기억하지 않으면 무한 루프를 돌 가능성이 높기 때문에.
'''
