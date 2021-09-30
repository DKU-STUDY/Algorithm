from collections import Counter

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    res = []
    for _ in range(N):
        res += list(map(int, input().split()))
    ranks = Counter(res).most_common()
    ranks.sort(key=lambda x: (-x[1], x[0]))

    second_rank_value = ranks[1][1]

    i = 1
    while i < len(ranks) and ranks[i][1] == second_rank_value:
        print(ranks[i][0], end=' ')
        i += 1
    print()
