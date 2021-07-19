def solution(s):
    answer = []
    
    for string in s:
        stack = []
        cnt_110 = 0
        for char in string:
            if char == '0' and stack[-2:] == ['1','1']:
                stack.pop()
                stack.pop()
                cnt_110 += 1
            else:
                stack.append(char)
        group_110 = '110' * cnt_110
        for idx in range(len(stack)-1,-1,-1):
            if stack[idx] == '0':
                stack.insert(idx+1, group_110)
                break
        else:
            stack.insert(0, group_110)    
        answer.append(''.join(stack))
        
    return answer