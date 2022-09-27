# 크레인이 N 대 있고, 1분에 박스를 하나씩 배에 실을 수 있다.
# 모든 크레인은 동시에 움직인다.
# 각 크레인은 무게 제한이 있다. 무게 제한 보다 무거운 박스는 크레인으로 움직일 수 없다.
# 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.
import heapq
import sys

crains_N = int(sys.stdin.readline())
crains = list(map(int, sys.stdin.readline().split()))
boxes_N = int(sys.stdin.readline())
boxes = list(map(lambda i: -int(i), sys.stdin.readline().split()))
heapq.heapify(boxes)

crains.sort(reverse=True)

res = 0
# 가장 무거운 박스를 가장 많이 드는 크레인이 못드는 경우
if -boxes[0] > crains[0]:
    print(-1)
    exit()

# 모든 박스를 시간이 오래걸려도 들을수있다.
while boxes:
    for crain in crains:
        if boxes:
            box = -heapq.heappop(boxes)
            if crain >= box:
                pass
            else:
                break
        else:
            break
    res += 1
print(res)
