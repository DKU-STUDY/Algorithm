from collections import defaultdict

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# meet in the middle
# N = 40 -> 20 두개로 쪼개면 시간 복잡도가 현저히 낮아진다.
# 2^40 -> 2^20 + 2^20
half = N // 2
arr1 = arr[:half]
arr2 = arr[half:]

arr1_dict = defaultdict(int)
arr2_dict = defaultdict(int)


# 1 ~ len 개 뽑는다.
def func(arr, dict, idx, s):
    if idx == len(arr):
        dict[s] += 1
        return

    # 뽑음
    func(arr, dict, idx + 1, s + arr[idx])
    # 뽑지 않음
    func(arr, dict, idx + 1, s)


func(arr1, arr1_dict, 0, 0)
func(arr2, arr2_dict, 0, 0)

res = 0
for key in arr1_dict:
    # 공집합 포함한다.
    res += arr1_dict[key] * arr2_dict[S-key]

if S == 0:
    # 공집합 * 공집합도 정답에 포함되므로 1 뺀다.
    res -= 1
print(res)