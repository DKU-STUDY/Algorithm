
n, c= map(int, input().split())
home= [int(input()) for _ in range(n)]
home.sort()

start, end= 1, home[-1]- home[0]
result= 0

while start <= end:
    mid= (start+ end)// 2

    val= home[0]
    cnt= 1
    for i in range(1, len(home)):
        if home[i] >= val+ mid:
            cnt+=1
            val= home[i]

    if cnt >= c:
        result= mid
        start= mid+ 1
    else: end= mid -1

print(result)