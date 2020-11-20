def solution(s):
    stack = []
    for i, n in enumerate(s):
        if n == '(':
            stack.append('(')
        elif n == ')':
            if stack == []:
                return False
            stack.pop()
    return stack == []

print(
    solution('()()') == True,
    solution('(())()') == True,
    solution(')()(') == False,
    solution('(()(') == False
)
