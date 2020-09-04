def solution(s):
    stack = []
    for i, n in enumerate(s):
        if n == '(':
            stack.append('(')
        elif n == ')':
            if stack != []:
                stack.pop()
            else:
                return False
    return True if stack == [] else False

print(
    solution('()()') == True,
    solution('(())()') == True,
    solution(')()(') == False,
    solution('(()(') == False
)