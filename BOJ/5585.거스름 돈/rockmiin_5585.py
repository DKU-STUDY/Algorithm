
x= int(input())
cnt=0
x= 1000-x
while(x>0):
    if x >= 500:
        x=x-500
    elif x >= 100:
        x=x-100
    elif x >= 50:
        x=x-50
    elif x >= 10:
        x=x-10
    elif x >= 5:
        x=x-5
    elif x >= 1:
        x=x-1
    else: break;
    cnt+=1
print(cnt)