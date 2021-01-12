
n= int(input())
arr= []
cnt= 0

for i in range(n):
    arr.append(list(map(int, input().split())))

# 첫번째 원소 기준으로 정렬을 해준 뒤 두번째 원소 기준으로 정렬을 해주는 것이 핵심
# print(arr)
arr.sort()
# print(arr)
arr.sort(key= lambda x: x[1])
# print(arr)

start, end= 0, 0

# 지금 하고 있는 회의의 종료 시점보다 arr값의 시작 값이 같거나 동일하다면 그 회의 시작, count
for i in range(n):
    x, y= arr[i][0], arr[i][1]
    if x>= end:
        start, end= x, y
        # print(start, end)
        cnt+=1
print(cnt)
