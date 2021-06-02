import collections

#0, 1은 필수
def bfs(s, t):
    Q = collections.deque()
    Q.append((s, ""))
    discovered = set()
    discovered.add(s)

# * + - /
    while Q:
        for _ in range(len(Q)):
            num, operator = Q.popleft()
            #뺄셈 나눗셈은 무조건 0,1이 된다. -> 연산하지 않는다.
            #곱/더하기/빼기/나누기 순
            #곱
            mul_n = num * num
            if mul_n == t:
                return operator + '*'
            elif mul_n < t and mul_n not in discovered:
                Q.append((mul_n, operator + '*'))
                discovered.add(mul_n)

            #더하기
            add_n = num + num
            if add_n == t:
                return operator + '+'
            elif add_n < t and add_n not in discovered:
                Q.append((add_n, operator + '+'))
                discovered.add(add_n)

            #나누기. 최초 1회수행
            if 1 not in discovered:
                Q.append((1, '/'))
                discovered.add(1)

    return -1


s, t = map(int, input().split())
if s == t:
    print(0)
elif t == 1:
    print('/')
else:
    print(bfs(s, t))

#소트 접근이 아니다.