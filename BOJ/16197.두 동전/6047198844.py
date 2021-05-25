import collections

buttons = [(0, -1), (0, 1), (-1, 0), (1, 0)] #y, x

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
coins = list()

for y in range(N):
    for x in range(M):
        if board[y][x] == 'o':
            coins.append((y, x))
# ((3, 0), (4, 0))
def bfs(coins):
    discovered = set()
    discovered.add(coins)
    queue = collections.deque()
    queue.append(coins)
    
    cnt = 0
    while queue and cnt < 10:
        cnt += 1
        n = len(queue)
        
        for _ in range(n):
            coin1, coin2 = queue.popleft()
            for button in buttons:
                dropped_coin = 0

                #새로운 동전의 위치
                new_coin1 = (coin1[0] + button[0], coin1[1] + button[1])
                new_coin2 = (coin2[0] + button[0], coin2[1] + button[1])

                ###############동전 위치 조정###############
                #동전 1이 떨어진 경우 / 범위를 벗어난 경우.
                if not(0 <= new_coin1[0] < N and 0 <= new_coin1[1] < M):
                    dropped_coin += 1

                #동전 1이 #인경우
                #버튼 조작을 취소한다.
                elif board[new_coin1[0]][new_coin1[1]] == '#':
                    new_coin1 = (coin1[0], coin1[1])

                #동전 2가 떨어진경우
                if not(0 <= new_coin2[0] < N and 0 <= new_coin2[1] < M):
                    dropped_coin += 1

                # 동전 2이 #인경우
                # 버튼 조작을 취소한다.
                elif board[new_coin2[0]][new_coin2[1]] == '#':
                    new_coin2 = (coin2[0], coin2[1])
                ###############위치 조정 종료###############
                ###############모든 조작이 완료된 상태###############

                ###############새로 방문할 필요가 있는지 판단###############
                # 예외처리 : 이미 발견한 경우 / 안 움직인 경우
                if (new_coin1, new_coin2) in discovered:
                    continue

                #하나도 안떨어진 경우 -> 재평가 / 새로운 발견
                if dropped_coin == 0:
                    queue.append((new_coin1, new_coin2))
                    discovered.add((new_coin1, new_coin2))

                #하나만 떨어진경우 -> 정답
                elif dropped_coin == 1:
                    return cnt # 실수한 부분 : while문에서 cnt의 범위를 cnt <= 10으로 잡으면 답이 11이 될수있다.
                #둘다 떨어진경우 -> 평가 종료.
    return -1
print(bfs(tuple(coins)))