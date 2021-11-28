import sys

n = int(sys.stdin.readline())
target = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
ans = []
cnt = 0
i = 1

for t in target:
    # 넣는 값이(i) 목표치보다 작을 경우. 무조건 stack에 없는 값이므로 i의 값까지 stack 에 계속 push 한다.
    while i <= t:
        ans.append('+')
        stack.append(i)
        i += 1

    # t의 값이 stack에서 나올때까지 stack에서 계속 꺼낸다.
    while stack:
        ans.append('-')
        if stack.pop() == t:
            cnt += 1
            break

if cnt == n:
    for a in ans:
        print(a)
else:
    print('NO')
