
n= int(input())

p=sorted(list(map(int, input().split())))
time=0
for i in range(n):
    time+=p[i]*(n-i)
print(time)
