# 이분 탐색 문제
# 이 술집에서 막걸리를 시키면 주전자의 용량은 똑같았으나 안에 들어 있는 막걸리 용량은 랜덤이다.
# 은상은 막걸리 N 주전자를 주문하고, 자신을 포함한 친구들 K 명에게 막걸리를 똑같은 양으로 나눠주려고 한다.
# 즉, 한 번 주문한 막걸리에 남은 것을 모아서 친구들에게 다시 주는 경우는 없다.
# 예를 들어 5명이 3 주전자를 주문하여 1002, 802, 705 ml의 막걸리가 각 주전자에 담겨져 나왔고, 이것을 401ml로 동등하게 나눴을 경우 각각 주전자에서 200ml, 0m, 304ml 만큼은 버린다.) 이럴 때
# K명에게 최대한의 많은 양의 막걸리를 분배할 수 있는 용량 ml는 무엇인지 출력해주세요.
#
# 입력
# 첫째 줄에는 은상이가 주문한 막걸리 주전자의 개수 N, 그리고 은상이를 포함한 친구들의 수 K가 주어진다.
# 둘째 줄부터 N개의 줄에 차례로 주전자의 용량이 주어진다. N은 10000이하의 정수이고, K는 1,000,000이하의 정수이다. 막걸리의 용량은 2^31 -1 보다 작거나 같은 자연수 또는 0이다.
# 단, 항상 N ≤ K 이다. 즉, 주전자의 개수가 사람 수보다 많을 수는 없다.
#
# 출력
# 첫째 줄에 K명에게 나눠줄 수 있는 최대의 막걸리 용량 ml 를 출력한다.
import sys

N, K = map(int, input().split())
arr = list(int(sys.stdin.readline()) for _ in range(N))

begin = 1
end = max(arr) + 1 # 주의 : upperbound

while begin < end:
    cnt = 0
    mid = (begin + end) // 2

    for num in arr:
        cnt += num // mid

    if K <= cnt:
        begin = mid + 1
    else:
        end = mid

print(end-1)
