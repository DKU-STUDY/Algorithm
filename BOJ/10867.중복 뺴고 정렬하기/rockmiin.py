
n= int(input())

arr= sorted(list(map(int, input().split())))
res= []

for i in arr:
    if i not in res:
        res.append(i)
        print(i, end=" ")