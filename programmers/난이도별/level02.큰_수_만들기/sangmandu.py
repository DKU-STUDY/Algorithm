'''
https://programmers.co.kr/learn/courses/30/lessons/42883
큰 수 만들기 : 순서를 지키면서 큰 수 만들기
수의 처음부터 비교해서 작은 수가 되면 k 횟수 안에서 pop
'''

def solution(number, k):
    stack = [number[0]]
    for i in number[1:]:
        while k > 0 and stack and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)
    if k != 0: stack = stack[:-k]
    return ''.join(stack)

'''
10번 시간초과 때문에 도저히 못풀어서 다른 코드 참조.
위 코드가 내 코드보다 훨씬 잘 풀었음.
'''