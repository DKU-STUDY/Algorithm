# 문제
# 민상이는 자신이 해야할 작업 N개를 아래와 같이 작업 순서도로 그려보았다.
# 작업 순서를 정할때 위배되는 작업 순서는 없다. 예를 들어, A 작업을 하려면 B 작업을 먼저 해야하고, B 작업을 해야하기 전에 A 작업을 해야하는 상황은 없다.
#
# 민상이는 오늘 반드시 끝낼 작업 X가 있다. 민상이가 작업 X 을 끝내기 위해서 먼저 해야하는 작업의 개수를 구해주자!
#
# 입력
# 민상이가 작업할 개수 N와 작업 순서 정보의 개수 M이 공백으로 구분되어 주어진다.
#
# 두 번째줄부터 M + 1 줄까지 작업 A_i와 작업 B_i가 공백으로 구분되어 주어진다. 이때 두 값의 의미는 작업 B_i를 하기 위해서 바로 이전에 작업 A_i를 먼저 해야한다는 의미이다. 중복된 정보는 주어지지 않는다.
#
# 마지막 줄에는 민상이가 오늘 반드시 끝내야하는 작업 X가 주어진다.
#
# 출력
# 민상이가 작업 X를 하기 위해 먼저 해야하는 일의 개수를 출력한다.
import sys
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(M):
    j, i = map(int, sys.stdin.readline().split())
    edges[i].append(j)
X = int(sys.stdin.readline())

Q = deque([X])
visited = {X}
res = 0

while Q:
    V = Q.popleft()

    for W in edges[V]:
        if W not in visited:
            Q.append(W)
            visited.add(W)
            res += 1

print(res)