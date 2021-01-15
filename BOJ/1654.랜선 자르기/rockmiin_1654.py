
k, n= map(int, input().split())
arr=[int(input()) for i in range(k)]

start= 1
end=max(arr)

result= 0

while(start <= end):
    cnt=0
    mid= (start+ end)// 2

    for i in arr:
        cnt+= i // mid

    if cnt >= n:
        start= mid+1
    else:
        end= mid- 1

print(end)