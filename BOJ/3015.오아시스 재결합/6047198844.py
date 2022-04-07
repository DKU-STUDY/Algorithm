# 문제
# 오아시스의 재결합 공연에 N명이 한 줄로 서서 기다리고 있다.
# 이 역사적인 순간을 맞이하기 위해 줄에서서 기다리고 있던 백준이는 갑자기 자기가 볼 수 있는 사람의 수가 궁금해 졌다.
# 두 사람 A와 B가 서로 볼 수 있으려면, 두 사람 사이에 A 또는 B보다 키가 큰 사람이 없어야 한다.
# 줄에 서있는 사람의 키가 주어졌을 때, 서로 볼 수 있는 쌍의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 줄에서 기다리고 있는 사람의 수 N이 주어진다. (1 ≤ N ≤ 500,000)
# 둘째 줄부터 N개의 줄에는 각 사람의 키가 나노미터 단위로 주어진다. 모든 사람의 키는 231 나노미터 보다 작다.
# 사람들이 서 있는 순서대로 입력이 주어진다.
#
# 출력
# 서로 볼 수 있는 쌍의 수를 출력한다.
import bisect
import sys

N = int(sys.stdin.readline())
left, right = 0, 0

arr = [int(sys.stdin.readline()) for _ in range(N)]

stack = []
res = 0
for i in arr:
    # 좌측보다 작은 경우.
    if stack and stack[-1] > i:
        res += 1
    # 좌측보다 같거나 큰 경우.
    else:
        while stack and stack[-1] < i:
           stack.pop()
           res += 1

        # 같은 경우가 있을 수 있다. 따라서 upper bound 를 통해. 개수를 알아낸다.
        if stack:
            begin = 0
            end = len(stack)
            target = i
            while begin < end:
                mid = (begin + end) // 2
                # 타겟이 더 큰경우 -> 타겟이 mid보다 왼쪽에 있다는뜻
                if stack[mid] > target:
                    begin = mid + 1
                else:
                    end = mid
            res += len(stack) - end
            if end != 0 and stack[end - 1] > target:
                res += 1

    stack.append(i)
print(res)