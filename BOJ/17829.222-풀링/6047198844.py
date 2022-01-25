# 문제
# 정사각형에서 2번째로 큰 수만 남긴다. 여기서 2번째로 큰 수란, 정사각형의 네 원소를 크기순으로 a4 ≤ a3 ≤ a2 ≤ a1 라 했을 때, 원소 a2를 뜻한다.
# 종욱이는 N×N 행렬에 222-풀링을 반복해서 적용하여 크기를 1×1로 만들었을 때 어떤 값이 남아있을지 궁금해한다.
#
# 입력
# 첫째 줄에 N(2 ≤ N ≤ 1024)이 주어진다. N은 항상 2의 거듭제곱 꼴이다. (N=2K, 1 ≤ K ≤ 10)
#
# 다음 N개의 줄마다 각 행의 원소 N개가 차례대로 주어진다. 행렬의 모든 성분은 -10,000 이상 10,000 이하의 정수이다.
#
# 출력
# 마지막에 남은 수를 출력한다.

def polling(arr):
    if len(arr) == 1:
        return arr[0][0]
    new_arr = list()
    # 새로운 어레이 구성
    for i in range(0, len(arr), 2):
        row = list()
        for j in range(0, len(arr[0]), 2):
            row.append(list(sorted([arr[i][j], arr[i][j + 1], arr[i + 1][j], arr[i + 1][j + 1]]))[2])
        new_arr.append(row)
    return polling(new_arr)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(polling(arr))
