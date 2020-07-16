def solution(arrangement):
    stack = []
    answer = 0
    arrangement = arrangement.replace("()", "|")
    for i in arrangement:
        if i == '(':
            stack.append(i)
        elif i == ')':
            stack.pop()
            answer += 1
        else:
            answer += len(stack)
    return answer
    
print(solution("()(((()())(())()))(())") == 17)
