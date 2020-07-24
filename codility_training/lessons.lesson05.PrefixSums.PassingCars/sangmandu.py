# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    zero_cnt = A.count(0)
    one_cnt = len(A)- zero_cnt
    cnt = 0
    for i in A:
        if i == 0:
            cnt += one_cnt
            zero_cnt -= 1
            continue
        one_cnt -= 1
    
    return cnt if cnt <= 1000000000 else -1

print(
    solution([0,1,0,1,1]) == 5
)