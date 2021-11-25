# 문제
# M개의 자연수로 이루어진 집합 S와 자연수 N이 주어진다.
#
# S에 속하지 않는 자연수 x, y, z를 골라서, |N - xyz|의 최솟값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000)과 집합 S의 크기 M(0 ≤ M ≤ 50)이 주어진다. 둘째 줄에는 집합 S에 들어있는 수가 주어진다. 집합에 들어있는 수는 1,000보다 작거나 같은 자연수이고, 공백으로 구분되어져 있다. 또, 중복되는 수는 없다.
#
# 집합의 크기가 0인 경우에는 둘째 줄은 빈 줄이다.
#
# 출력
# 첫째 줄에 |N - xyz|의 최솟값을 출력한다.
N, M = map(int, input().split())
S = set(map(int, input().split()))
ans = 987654321
for x in range(1, 1000 + 1):
    if x in S:
        continue
    for y in range(x, 1000 + 1):
        if y in S:
            continue
        for z in range(y, 1001 + 1):
            if z in S:
                continue
            ans = min(ans, abs(N - x*y*z))
print(ans)