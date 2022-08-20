import sys

n = int(sys.stdin.readline())
mentions = list(map(int, sys.stdin.readline().split()))

for k in range(len(mentions), -1, -1):
    # k번 이상 인용된 논문이 k편 이상이고 나머지 n − k 편의 논문들 인용회수가 각각 k 번 이하라면, 해당 학생의 q-인덱스는 k이다.
    upper_cnt = 0
    lower_cnt = 0
    for mention in mentions:
        if mention >= k:
            upper_cnt += 1
        if mention <= k:
            lower_cnt += 1

    if k <= upper_cnt and len(mentions) - k <= lower_cnt:
        print(k)
        exit()