def solution(S):
    # write your code in Python 3.6
    braket_stack =[]
    parentheses = "("
    curly = "{"
    square ="["
    for i in S:
        if i == '(':
            braket_stack.append(parentheses)
        if i == ')':
            if len(braket_stack) == 0:
                return 0
            elif braket_stack[-1] == parentheses:
                braket_stack.pop()
            else:
                return 0

        if i == '{':
            braket_stack.append(curly)
        if i == '}':
            if len(braket_stack) == 0:
                return 0
            elif braket_stack[-1] == curly:
                braket_stack.pop()
            else:
                return 0

        if i == '[':
            braket_stack.append(square)
        if i == ']':
            if len(braket_stack) == 0:
                return 0
            elif braket_stack[-1] == square:
                braket_stack.pop()
            else:
                return 0
    if len(braket_stack) == 0:
        return 1
    else:
        return 0
