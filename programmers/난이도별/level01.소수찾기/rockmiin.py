# 에라토스테네스의 체 이용
def solution(n):
    arr=[0,0]+[1]*(n-1)
    for i in range(2, n+1):
        if arr[i]==1:
            for j in range(2*i, n+1, i):
                arr[j]=0
    return sum(arr)

print(
    solution(10)==4
)