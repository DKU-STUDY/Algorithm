
n= int(input())

min= 5000

for i in range((n//5)+1):
    if n%3==0 and n//3 < min:
        min= (n//3) + i
    n-=5
if min== 5000:
    min= -1

print(min)

