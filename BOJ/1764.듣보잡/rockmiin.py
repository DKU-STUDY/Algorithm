
n, m= map(int, input().split())
arr= []
res= []

for i in range(n+m):
    arr.append(input())
arr.sort()
# print(arr)
for i in range(1, n+m):
    if arr[i-1] == arr[i]:
        res.append(arr[i])

print(len(res))
for i in range(len(res)):
    print(res[i])

# 입력 예시
# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton

# 출력 예시
# 2
# baesangwook
# ohhenrie