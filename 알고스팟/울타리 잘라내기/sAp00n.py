"""
N 개의 늘어져 있는 각자 다른높이의 울타리에서 잘라낼 수 있는 가장 큰 넓이를 구하는 문제.

N = 2 * 10^4
시간제한은 1sec 이므로,
1 * 10^8 / 2 * 10^4(N) = 대락 O(N^2)복잡도 이하로 작성되어야 한다

하지만.... O(N!*N) 밖에 생각나지 않는다..

-- 이해 완료 --

이해 후에 해답 안보고 다시 코드 작성하다가 머리 터질뻔함;;
idx의 오른쪽만 열린방향으로 코드를 작성하기가 왤캐 힘드냐

"""

from sys import stdin


def recursion_slice(left, right):
    global list_of_fence

    if left == right:
        return list_of_fence[left]

    mid_idx = (left + right) // 2

    recursion_max = max(recursion_slice(left, mid_idx), recursion_slice(mid_idx + 1, right))

    height = min(list_of_fence[mid_idx], list_of_fence[mid_idx + 1])
    mid_max = height
    left_idx, right_idx = mid_idx, mid_idx + 1
    while left < left_idx and right_idx < right:
        if right_idx < right:
            if list_of_fence[right_idx + 1] >= list_of_fence[left_idx - 1]:
                right_idx += 1
                height = min(height, list_of_fence[right_idx])
                mid_max = max(mid_max, height * (right_idx + 1 - left_idx))
                continue
        left_idx -= 1
        height = min(height, list_of_fence[left_idx])
        mid_max = max(mid_max, height * (right_idx + 1 - left_idx))
    return max(recursion_max, mid_max)


C = int(stdin.readline())  # test case 의 개수

for i in range(C):
    N = int(stdin.readline())  # 판자의 개수
    global list_of_fence
    list_of_fence = list(map(int, stdin.readline().split()))
    print(recursion_slice(0, N - 1))
