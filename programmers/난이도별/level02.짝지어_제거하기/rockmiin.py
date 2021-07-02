from collections import deque

def solution(s):

    arr= list(s)
    if len(arr)== 1:
        return 0

    left_q, right_q= deque(), deque()
    left_q.append(s[0])
    for i in range(1, len(arr)):
        right_q.append(arr[i])

    while right_q:
        # print(left_q, right_q)
        if len(left_q)== 0:
            if len(right_q)> 1:
                left_q.append(right_q.popleft())
            else:
                left_q.append(right_q.popleft())
                break;
        if left_q[-1]== right_q[0]:
            left_q.pop(); right_q.popleft()
        else: left_q.append(right_q.popleft())

    if len(left_q)== 0:
        return 1
    return 0


solution('aaaab')


