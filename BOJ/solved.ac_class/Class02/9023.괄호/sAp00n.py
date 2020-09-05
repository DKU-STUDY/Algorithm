from sys import stdin
from collections import deque


def checker(test_case):
    que = deque()
    for idx in range(len(test_case)):
        if test_case[idx] == ')':
            if '(' not in que:
                return False
            que.remove('(')
        if test_case[idx] == '(':
            que.appendleft('(')
    return len(que) == 0


T = int(stdin.readline())
str_list = [stdin.readline().rstrip('\n') for string in range(T)]

for test_case in str_list:
    if checker(test_case):
        print('YES')
    else:
        print('NO')
