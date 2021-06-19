import collections

table = {
    '{' : '}',
    '[' : ']',
    '(' : ')'
}


def is_valid(word):
    stack = []
    
    for char in word:
        if char == '[' or char == '(' or char == '{':
            stack.append(char)
        else:
            #stack이 비엇거나. 짝이 아닐경우.
            if not stack or char != table[stack.pop()]:
                return False
    if stack:
        return False
    else:
        return True
    
    
    
def solution(s):
    answer = 0
    
    #홀수이면 올바른 괄호 문자열이 아니다.
    if len(s) % 2 == 1:
        return answer
    
    
    Q = collections.deque(s)
    for _ in range(len(s)):
        answer += is_valid(''.join(Q))
        Q.rotate(1)
    
    
    return answer