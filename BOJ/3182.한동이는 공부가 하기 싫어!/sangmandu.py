'''
https://www.acmicpc.net/problem/3182
한동이는 공부가 하기 싫어!
[풀이]
1. 인덱스를 맞춰주기 위해 입력값 - 1을 리스트에 저장
2. 각자 연결되는 사람 수를 저장하기 위한 cost 리스트
3. 모든 사람을 기준으로 한사람씩 연결되는 사람수를 계산하기 위한 반복문
'''
n = int(input())
lst = [int(input())-1 for _ in range(n)]
cost = [0] * n
for idx in range(n):
    stack = [idx]
    visited = [0] * n
    visited[idx] = 1
    while stack:
        src = stack.pop()
        dst = lst[src]
        if not visited[dst]:
            visited[dst] = 1
            stack.append(dst)
            cost[idx] += 1
print(cost.index(max(cost))+1)