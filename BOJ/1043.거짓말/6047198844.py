# 문제
# 진실을 아는 사람이 있을때는 거짓말을 못한다.
# 거짓말을 들었던 사람이 있을때는 거짓말을 못한다.
# 거짓말을 할 수 있는 파티 개수의 최댓값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다.
# 둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다. 진실을 아는 사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다. 사람들의 번호는 1부터 N까지의 수로 주어진다.
# 셋째 줄부터 M개의 줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다.
#
# N, M은 50 이하의 자연수이고, 진실을 아는 사람의 수는 0 이상 50 이하의 정수, 각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.
#
# 출력
# 첫째 줄에 문제의 정답을 출력한다.

# 루트를 찾는다.
def find(n):
    # 자신이 루트인가
    if P[n] < 0:
        # 자신을 반환한다.
        return n
    # 자기 부모로 이동, 루트를 찾는다.
    P[n] = find(P[n])
    return P[n]


# a와 b를 합친다.
def union(a, b):
    ra = find(a)
    rb = find(b)
    # 루트가 같은지 확인한다.
    if ra == rb:
        return
    # rb의 부모가 ra가 된다. -> rb의 루트가 ra가 된다.
    P[rb] = ra


# N : 사람의 수 M : 파티의 수
# 1 <= N, M <= 50
# 입력
N, M = map(int, input().split())
_, *known_people = map(int, input().split())
parties = []
for _ in range(M):
    _, *party = map(int, input().split())
    parties.append(party)

P = [-1 for _ in range(N + 2)]

# union. 같은 파티에 있다면, 같은 소속이다. 같은 소속은 같이 진실을 알거나, 같이 진실을 몰라야한다.
# 소속 : 진실을 아는 사람의 집합 / 진실을 알수없는 사람들의 집합
for i in range(len(parties)):
    # 각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.
    root = find(parties[i][0])
    for j in range(1, len(parties[i])):
        union(root, parties[i][j])

# find.
# 현재 파티에 참가한사람이 진실을 아는 사람의 집합에 속해 있는지 확인한다.
# 속해 있다면 거짓말을 칠수없다.
res = 0
for i in range(len(parties)):
    # 한명이라도 진실을 알면 True, 모두 진실을 모르면 False
    flag = False
    for j in range(len(parties[i])):
        for known_person in known_people:
            # 루트가 같다면, 같은 집합 소속이다.
            if find(parties[i][j]) == find(known_person):
                flag = True
                break
        if flag:
            break
    if not flag:
        res += 1
print(res)
