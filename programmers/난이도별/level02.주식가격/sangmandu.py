'''
https://programmers.co.kr/learn/courses/30/lessons/42584
주식가격 : 특정 인덱스의 값이 이 인덱스 이후의 값들 보다 작을 때 이후의 값의 갯수 구하기
case 수가 100,000개 이므로 O(n^2)으로 구현하지 않도록 한다. 스택을 사용해서, 갯수 조사
'''

def solution(prices):
    stack = [(prices[-2],1)]
    answer = [0,1]
    for i in prices[-3::-1]:
        if i > stack[-1][0]:
            answer.append(1)
            stack.append((i,1))
            continue
        cnt = 1
        while stack and i <= stack[-1][0]:
            cnt += stack[-1][1]
            stack.pop()
        answer.append(cnt)
        stack.append((i, cnt))
    return answer[::-1]


'''
테스트 케이스는 100,000개 인데 이중 반복문으로 구현해도 통과가 되는 이상한 문제
'''