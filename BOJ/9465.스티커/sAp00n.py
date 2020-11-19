# 실패한 아이디어들...
# 1. 가장 큰 값의 스티커를 일단 뜯어 낸 후, 반으로 갈라진 스티커들을 재귀적으로 계산 = > 메모리 오버.
# 2. 부루트포스 방식으로 접근하되, 한번 접근한 노드에 대한 최댓값을 메모이제이션 시켜 그보다 적을경우 큐에 추가하지 않음 => 메모리 오버
# 3. 결국 솔루션 보고 일반항을 세울수 있다는걸 알게됨... 왜 몰랐을까
from sys import stdin


def sol():
    n = int(stdin.readline())
    sticker = [list(map(int, stdin.readline().split())) for _ in range(2)]

    DP = {(0, 0): sticker[0][0], (1, 0): sticker[1][0], (0, 1): sticker[1][0] + sticker[0][1],
          (1, 1): sticker[0][0] + sticker[1][1]}

    for idx in range(2, n):
        DP[(0, idx)] = max(DP[(1, idx - 1)], DP[(1, idx - 2)]) + sticker[0][idx]
        DP[(1, idx)] = max(DP[(0, idx - 1)], DP[(0, idx - 2)]) + sticker[1][idx]

    return max(DP[(0, n - 1)], DP[(1, n - 1)])


T = int(stdin.readline())

for _ in range(T):
    print(sol())
