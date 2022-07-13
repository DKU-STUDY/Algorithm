N, K = map(int, input().split())
num = list(input())
k, stack = K, []
for i in range(N):
    while k > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        k -= 1
    stack.append(num[i])
print(''.join(stack[:N-K]))