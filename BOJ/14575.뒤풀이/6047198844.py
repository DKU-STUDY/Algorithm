# 문제
#
# 도현이는 우선 각 사람에게 어느 정도 마시면 기분이 좋은지(Li)와, 어느 정도 마시면 힘든지(Ri)를 물어보았다.
# 도현이는 정확히 T의 술을 결제하였다.
# 이제 도현이는 모든 사람 i에게 Li이상 Ri이하의 술을 주면서, 그 총합이 정확히 T가 되도록 술을 분배하려고 한다.
# 도현이는 S의 값을 정하고, 각 사람에게 그 사람이 원하는 술의 양이 얼마이던지 관계없이 S이하의 술만을 주려고 한다.
# 모든 사람 i가 Li이상 Ri이하의 술을 받으면서,
# 모든 사람이 받은 술의 총합이 정확히 T가 되고,
# 어떤 사람도 S를 초과하는 술은 받지 않게 할 수 있는,
# 그러한 S값만 결정하면 된다.
# 도현이를 도와 조건을 만족하는 S값을 찾아주도록 하자.
# 만약 그런 값이 여러 개라면, 도현이는 그 중 가장 작은 값을 찾고 싶다.
#
# 입력
# 첫째 줄에 대회 참가자의 수 N과 술의 총량 T가 주어진다. (1 ≤ N ≤ 1000, 1 ≤ T ≤ 10^9)
#
# 둘째 줄부터 N개의 줄에 걸쳐, 각 사람에 대한 Li와 Ri값이 주어진다. (1 ≤ Li ≤ Ri ≤ 106)
#
# 출력
# 만약 S의 값과는 관계없이 항상 불가능하다면 첫째 줄에 -1만을 출력한다.
#
# 문제의 조건을 만족하는 S값이 존재한다면 가장 작은 값 하나를 출력한다.

N, T = map(int, input().split())

drinks = [tuple(map(int, input().split())) for _ in range(N)]

min_list, max_list = zip(*drinks)
min_sum = sum(min_list)
max_sum = sum(max_list)
# 최저로 소비 || 최대로 소비
if min_sum > T or max_sum < T:
    print(-1)
    exit()

begin = min(min_list)
end = max(max_list) + 1


def is_possible(S):
    more = 0
    for L, R in drinks:
        if S < L:
            return False
        more += min(S, R) - L
    return more >= T - min_sum


while begin < end:
    mid = (begin + end) // 2
    # 가능하지? 가능하다면 범위를 좁힌다.
    if is_possible(mid):
        end = mid
    else:
        begin = mid + 1

print(end)
