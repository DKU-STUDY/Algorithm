sentence = input()
N = len(sentence)
stack = []
res = ''


def priority(op):
    if op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    elif op == '(' or op == ')':
        return 0
    return -1


for i in range(N):
    # 알파벳인 경우
    if sentence[i].isalpha():
        res += sentence[i]

    # 괄호인 경우
    elif sentence[i] == '(':
        stack.append(sentence[i])
    elif sentence[i] == ')':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.pop()

    # 연산자인 경우
    else:
        while stack and priority(stack[-1]) >= priority(sentence[i]):
            res += stack.pop()
        stack.append(sentence[i])

res += ''.join(stack[::-1])
print(res)