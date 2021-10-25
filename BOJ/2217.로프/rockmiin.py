
n= int(input())
row=sorted([int(input()) for i in range(n)])
max_weight= 0

for i in range(n):
    if row[i]*(n-i) > max_weight:
        max_weight= row[i]*(n-i)
print(max_weight)

# 입력받은 row를 무게 기준으로 정렬을 한 뒤에 비교 (row를 전부 쓸 필요가 없기 때문에 row를 일부만 사용하는 경우 고려)

# 예제 입력
# 2
# 10
# 15
#
# 예제 출력
# 20