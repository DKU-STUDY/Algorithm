def solution():
    t= int(input())
    for _ in range(t):
        n= int(input())
        score= []

        for i in range(n):
            score.append(list(map(int, input().split())))
        score.sort()

        cnt= 1
        tmp= 0
        for i in range(1, n):
            if score[tmp][1] > score[i][1]:
                tmp= i; cnt+=1
        print(cnt)

solution()