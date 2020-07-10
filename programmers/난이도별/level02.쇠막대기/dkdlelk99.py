def solution(arrangement):
    index = []
    stack = []
    answer = 0
    arrangement = arrangement.replace("()", "|")
    
    # (에 대응하는 ) 찾아서 인덱싱
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            index.append(i)
        elif arrangement[i] ==')':
            stack.append([index.pop(), i])        
    
    # 막대기 양끝 사이에 몇개의 레이저가 있는지 검사
    for len_of_stick in stack:
        raser = 1
        for text in range(len_of_stick[0],len_of_stick[1]):
            if arrangement[text] == '|':
                raser += 1
        answer += raser
             
    return answer
    
print(solution("()(((()())(())()))(())") == 17)
