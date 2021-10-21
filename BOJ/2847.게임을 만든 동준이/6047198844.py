import sys

#input
N = int(sys.stdin.readline())
levels = list()
for _ in range(N):
    levels.append(int(sys.stdin.readline()))

#뒤집어서 생각
levels.reverse()

#로직 -> 이전 값보다 1작게 . 이전값보다 이미 작으면 그대로.
res = 0
for idx in range(1,len(levels)):
    # 현재값이 크면안된다. 현재값은 이전값 -1 보다 같거나 작아야한다.
    if levels[idx-1] - 1 < levels[idx]:
        #현재값 - (이전값 - 1) 을 res에 더한다.
        res += levels[idx] - (levels[idx-1] - 1)
        #현재값을 이전값 -1 로 맞춘다.
        levels[idx] = levels[idx-1] - 1

#output
print(res)