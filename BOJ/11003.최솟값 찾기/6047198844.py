# 문제
# N개의 수 A1, A2, ..., AN과 L이 주어진다.
#
# Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.
#
# 입력
# 첫째 줄에 N과 L이 주어진다. (1 ≤ L ≤ N ≤ 5,000,000)
#
# 둘째 줄에는 N개의 수 Ai가 주어진다. (-109 ≤ Ai ≤ 109)
#
# 출력
# 첫째 줄에 Di를 공백으로 구분하여 순서대로 출력한다.

# 최소값 / 최소값 후보
from collections import deque

N, L = map(int, input().split())
arr = list(map(int, input().split()))

res = deque([])
for i, num in enumerate(arr):
    # res 최적화. 현재 범위에 맞지 않는 경우를 모두 없엔다.
    while res and not (i-L+1 <= res[0][0] <= i):
        res.popleft()

    # res가 없으면 삽입 -> 무조건 최소값임.
    if not res:
        res.append((i, num))
    # res의 길이가 1이면 삽입 -> 무조건 최소값 또는 최소값 후보임.
    elif len(res) == 1:
        if res[0][1] >= num:
            res.appendleft((i, num))
        else:
            res.append((i, num))

    # res의 길이가 2일때.
    # 현재값이 최소값이 될수도 있고, 최소값의 후보가 될수있다. 또 아무것도 아닐수도 있다.
    else:
        # 최소값인 경우
        if res[0][1] >= num:
            res.popleft()
            res.appendleft((i, num))

        # 최소값의 후보인 경우
        elif res[1][1] >= num:
            res.pop()
            res.append((i, num))
    print(res[0][1], end=' ')
