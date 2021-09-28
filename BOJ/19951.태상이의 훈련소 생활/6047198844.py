"""
문제
연병장은 일렬로 이어진 N개의 칸으로 이루어져 있으며 각 칸마다 높이를 가지고 있고, 첫 번째 칸부터 순서대로 1번, 2번, 3번, ..., N번 칸으로 명칭이 붙어있다.
조교들은 총 M명이 있으며, 각 조교들은 태상이에게 a번 칸부터 b번 칸까지 높이 k만큼 흙을 덮거나 파내라고 지시한다. 흙은 주변 산에서 얼마든지 구할 수 있으므로 절대로 부족하지 않다.

태상이는 각 조교의 지시를 각각 수행하면, 다른 조교의 지시로 흙을 덮어둔 칸을 다시 파내기도 하는 비효율적인 일이 발생하는 것을 깨달았다.
그래서 태상이는 각 조교의 지시를 모아 연병장 각 칸의 최종 높이를 미리 구해 한 번에 일을 수행하려고 한다.

불쌍한 태상이를 위해 조교들의 지시를 모두 수행한 뒤 연병장 각 칸의 높이를 구하자.

입력
첫 줄에 연병장의 크기 N과 조교의 수 M이 주어진다.

둘째 줄에 연병장 각 칸의 높이 Hi가 순서대로 N개 주어진다.

셋째 줄부터 M개의 줄에 각 조교의 지시가 주어진다.

각 조교의 지시는 세 개의 정수 a, b, k로 이루어져 있다.

k ≥ 0인 경우 a번 칸부터 b번 칸까지 높이가 각각 |k| 만큼 늘어나도록 흙을 덮어야 한다.
k < 0인 경우 a번 칸부터 b번 칸까지 높이가 각각 |k| 만큼 줄어들도록 흙을 파내야 한다.

초기 연병장의 상태: 1 2 3 4 5 -1 -2 -3 -4 -5
첫번째 지시 (1 5 -3)를 수행 한 뒤: -2 -1 0 1 2 -1 -2 -3 -4 -5
두번째 지시 (6 10 5)를 수행한 뒤: -2 -1 0 1 2 4 3 2 1 0
세번째 지시 (2 7 2)를 수행한 뒤: -2 1 2 3 4 6 5 2 1 0

(1 5 -3)
(6 10 5)
(1 1 -3) , (2 5 -1) , (6 7 7) (8 10 5)

교집합은 갱신. 이외는 갱신 X -> 하지만 범위를 다시 설정한다.
교집합
"""
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
H = list(map(int, sys.stdin.readline().rstrip().split()))
variance = [0 for _ in range(N+1)]

for _ in range(M):
    # a부터 시작해서 b까지 증가. 이를 증감량으로 표현하면. a에서 증가 +K , b+1 에서 -K로 표현가능하다.
    a, b, k = tuple(map(int, sys.stdin.readline().rstrip().split()))
    variance[a-1] += k
    variance[b] += -k

for i in range(1, N+1):
    variance[i] += variance[i-1]
    H[i-1] += variance[i-1]
print(variance)
print(H)
