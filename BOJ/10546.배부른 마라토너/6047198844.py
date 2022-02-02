# 문제
# ㅂㅐㄱ준 마라톤 대회에 참가해 놓고 완주하지 못한 배부른 참가자 한 명은 누굴까?
#
# 입력
# 첫째 줄에는 참가자 수 N이 주어진다. (1 ≤ N ≤ 10^5)
# N개의 줄에는 참가자의 이름이 주어진다.
# 추가적으로 주어지는 N-1개의 줄에는 완주한 참가자의 이름이 쓰여져 있다.
# 참가자들의 이름은 길이가 1보다 크거나 같고, 20보다 작거나 같은 문자열이고, 알파벳 소문자로만 이루어져 있다.
# 참가자들 중엔 동명이인이 있을 수도 있다.
#
# 출력
# 마라톤을 완주하지 못한 참가자의 이름을 출력한다.
import sys
from collections import Counter

N = int(input())
players = [sys.stdin.readline().rstrip() for _ in range(N + N - 1)]
for player, count in Counter(players).items():
    if count % 2 == 1:
        print(player)
        break