# 소들은 정보섬 1층 앞마당에서 A1, A2, A3, ..., AN, A1의 순서대로 동그랗게 앉아 쉬고 있다.
# 각 소들에게는 품질 점수 Ai가 적힌 스티커가 붙어 있다.
# 풀어 쓰자면, 원형으로 둘러 앉은 소들에 대해서, 연속한 네 마리 소들의 품질 점수를 곱한 값을 모두 (정확히 한 번씩) 더한 것이다.
# 욱제는 총 Q번에 걸쳐 어떤 i번째 소를 선택할 것이다. 그러고는 Ai가 적힌 스티커를 떼어내고, Ai*(-1)이 적힌 스티커를 붙일 작정이다.

# i 번째 소는 몇번째 그룹에 속할까?
# A1 그룹 / A2 그룹 / A3 그룹 / ... / A8 그룹
# i를 3이라고 하면, A3 그룹 / A2 그룹 / A1 그룹 / A8 그룹에 속할것이다. 스티커가 바꿔치기 당했을때 해당 그룹 계산만 다시해주면 된다.
# Ai / Ai-1 / Ai-2 / Ai-3

# 입력
# 첫째 줄에 소의 수를 나타내는 N과 욱제가 장난칠 횟수 Q가 주어진다. (4 ≤ N ≤ 200,000, 1 ≤ Q ≤ 200,000)
#
# 둘째 줄에 N마리 소들의 품질 점수 Ai가 순서대로 주어진다. (1 ≤ |Ai| ≤ 10)
#
# 셋째 줄에 욱제가 장난칠 Q개의 소의 번호가 순서대로 주어진다. (1 ≤ Qi ≤ N)
#
# 출력
# Q개의 줄에 걸쳐 다시 계산된 S의 값을 출력한다.

N, Q = map(int, input().split())
cow_scores = list(map(int, input().split()))
fake_idxes = list(map(int, input().split()))

cow_groups = [cow_scores[i % N] * cow_scores[(i + 1) % N] * cow_scores[(i + 2) % N] * cow_scores[(i + 3) % N] for i in
              range(N)]
res = sum(cow_groups)

for idx in fake_idxes:
    idx = idx - 1
    desc = 0
    for i in range(idx, idx - 4, -1):
        cow_groups[i % N] = - cow_groups[i % N]
        desc += cow_groups[i % N]
    res += 2 * desc
    print(res)
