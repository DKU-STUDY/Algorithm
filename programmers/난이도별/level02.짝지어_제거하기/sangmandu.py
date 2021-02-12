'''
https://programmers.co.kr/learn/courses/30/lessons/12973
짝찌어 제거하기
stack을 이용
'''

def solution(s):
    stack = [s[0]]
    for i in s[1:]:
        if not stack or stack[-1] != i:
            stack.append(i)
            continue
        stack.pop()
    return 1 if not stack else 0


'''
나보다 잘 푼 사람은 없는 듯
'''