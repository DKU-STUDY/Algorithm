import sys

sys.setrecursionlimit(10 ** 7)


def solution(sticker):
    answer = 0

    if len(sticker) == 1:
        return sticker[0]

    def dp(idx, sticker, memo):
        if idx >= len(sticker):
            return 0
        # 현재스티커포함
        # + 다다음 스티커의 경우의수
        if memo[idx] != 0:
            return memo[idx]

        memo[idx] = max(sticker[idx] + dp(idx + 2, sticker, memo), sticker[idx] + dp(idx + 3, sticker, memo))
        return memo[idx]

    memo1 = [0] * len(sticker)
    memo2 = [0] * len(sticker)

    # 첫번째 스티커 땐경우 / 두번째 스티커 땐경우 / 세번째 스티커 땐경우
    answer = max(dp(0, sticker[:-1], memo1), dp(1, sticker, memo2), dp(2, sticker, memo2))

    return answer