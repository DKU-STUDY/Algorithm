# 민식이는 아이들에게 선물할 같은 크기의 작은 박스를 N개 가지고 있다.
# 모든 작은 박스는 "정육면체"이고, 크기는 A × A × A 이다.
# 민식이는 이 작은 박스를 크기가 L × W × H 인 직육면체 박스에 모두 넣으려고 한다.
# 모든 작은 박스는 큰 박스 안에 있어야 하고, 작은 박스의 변은 큰 박스의 변과 평행해야 한다.
#
# N, L, W, H가 주어질 때, "가능한 A의 최댓값을 찾는 프로그램"을 작성하시오.

N, L, W, H = map(int, input().split())

# 최소값?
begin = 0
# 최대값 / min 아닌가?.......
end = min(L, W, H)

for _ in range(10000):
    mid = (begin + end) / 2
    box_N = (L // mid) * (W // mid) * (H // mid)

    if N <= box_N:
        begin = mid
    else:
        end = mid

print("%.10f" %(end))