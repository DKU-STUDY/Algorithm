import sys

N, K = map(int, input().split())
tops = list(map(int, input().split()))
res = sys.maxsize
for idx in range(N):
    # 기준항 = tops[idx] = 변경되면 안되는 값
    # 초항은 ? tops[idx] - (K * idx)
    fir = tops[idx] - (K * idx)
    # 초항을 기준으로 만들어짐.
    # 마지막항은 ? 초항 + (K * N)
    # 만들어지는 배열은?
    # 탑의 높이....... 즉 음수는 될수없다.
    if fir < 1:
        continue
    blocks = list(range(fir, fir + (K * N), K))
    dif = 0
    for top, block in zip(tops, blocks):
        dif += bool(top != block)
    else:
        res = min(res, dif)
print(res)