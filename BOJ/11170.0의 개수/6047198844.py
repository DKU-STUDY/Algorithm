T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(sum([str(i).count("0") for i in range(N, M + 1)]))
