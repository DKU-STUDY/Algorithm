# () 닫을때 현재값 x 2
# [] 닫을때 현재값 x 3
s = list(input())
stack = []
tmp = 1
res = 0
for i in range(len(s)):
    if s[i] == '(':
        tmp *= 2
        stack.append('(')
    elif s[i] == '[':
        tmp *= 3
        stack.append('[')
    elif s[i] == ')':
        if stack and stack[-1] == '(':
            if s[i - 1] == '(':
                res += tmp
            stack.pop()
            tmp = tmp // 2
        else:
            print(0)
            exit()
    elif s[i] == ']':
        if stack and stack[-1] == '[':
            if s[i - 1] == '[':
                res += tmp
            stack.pop()
            tmp = tmp // 3
        else:
            print(0)
            exit()
print(res)