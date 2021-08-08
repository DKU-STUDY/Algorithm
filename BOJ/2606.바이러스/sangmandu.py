'''
https://www.acmicpc.net/problem/2606
바이러스
[풀이]
1. 각 노드간의 관계를 표현하기 위해 defaultdict 사용
2. 방문관계를 나타내기 위한 visited 선언
=> 1번 노드부터 바이러스가 퍼지므로 1번은 방문한 것으로 초기화
=> 0번 노드는 인덱스간의 비교를 위한 용도로만 사용
3. DFS : 스택에서 뽑은 기준노드 그리고 기준노드와 연결되어있는 노드 조사
=> 연결노드를 이미 방문했다면 패스
=> 연결노드를 방문하지 않았다면 방문 마킹
=> 연결노드와 또 연결된 노드들을 조사하기 위해 stack에 append
4. 1을 제외한 감염 컴퓨터 반환
'''
from collections import defaultdict
n, m = map(int, [input(), input()])
dic = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

visited = [0, 1] + [0] * (n-1)
stack = [1]
while stack:
    idx = stack.pop()
    for node in dic[idx]:
        if not visited[node]:
            visited[node] = 1
            stack.append(node)
print(visited.count(1)-1)
