# 문제
# Moo 수열은 다음과 같은 방법으로 재귀적으로 만들 수 있다.
# 먼저, S(0)을 길이가 3인 수열 "m o o"이라고 하자.
# k >= 1 , S(k) =  S(k-1) + o가 k+2개인 수열 "m o ... o" + S(k-1)
# S(0) = "m o o"
# S(1) = "m o o m o o o m o o"
# S(2) = "m o o m o o o m o o m o o o o m o o m o o o m o o"
# S(3) = "m o o m o o o m o o m o o o o m o o m o o o m o o m o o o o o m o o m o o o m o o m o o o o m o o m o o o m o o"
# 위와 같은 식으로 만들면, 길이가 무한대인 문자열을 만들 수 있으며, 그 수열을 Moo 수열이라고 한다.
# N이 주어졌을 때, Moo 수열의 N번째 글자를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N (1 ≤ N ≤ 10^9)이 주어진다.
#
# 출력
# N번째 글자를 출력한다.

# func(N, K, length)
# N : N번째 글자
# K : 현재 수열의 번호
# length : 현재 수열의 길이
def func(N, K, length):
    # m o o 만 남았을떄.
    if N <= 3:
        return ("moo"[N - 1])

    next_length = length * 2 + K + 3

    # 확장한다.
    if next_length < N:
        return func(N, K + 1, next_length)

    # 다음 Moo 의 범위에 속해있는지 확인한다.
    if length + 1 <= N <= length + K + 3:
        return "m" if N == length + 1 else "o"

    # 재귀를 처음부터 다시 시작한다. N의 범위는 줄어든다.
    return func(N - (length + K + 3), 1, 3)


print(func(int(input()), 1, 3))
