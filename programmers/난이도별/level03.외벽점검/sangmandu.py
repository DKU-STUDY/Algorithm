'''
https://programmers.co.kr/learn/courses/30/lessons/60062
외벽 점검
[풀이]
1. 몇개의 변수를 세팅해준다
1-1. 원래 week 길이를 기억하기 위한 W
1-2. 시계방향 또는 반시계방향으로 이동 가능한 것은 시계방향으로만 이동해도 무관하다
=> 방향을 고려하지 않기 위해 weak을 확장 n만큼 더해준 수만큼을 추가한다
1-3. 각 지점에서 다음 지점까지의 차이를 구한 diff
1-4. 추후에, 친구들이 이동한 거리들을 구할 것이다.
=> 이 때, 친구들이 이동한 거리가 [5, 4, 3]이고 dist가 [6, 4, 2] 라고 하자
=> 그러면 친구들이 이동한 거리 [5, 4, 3]은 실제로 이동할 수 없는 거리이다
=> 왜냐하면 6과 4는 같은 인덱스 위치인 5와 4보다 같거나 크지만, 2는 3보다 작기 때문
=> 이렇게, 내림차순으로 정렬해서 같은 인덱스 값을 비교함으로써 수리 여부를 판단할 수 있다
=> 따라서 dist를 미리 오름차순 정렬한다.
2. 어떤 점부터 시작할 지 모르니 모든 점이 시작점이 되도록 반복문을 작성
=> diff는 2n-1개만큼 존재하지만 실제로 n-1개만 고려할 것이다.
=> diff가 2n-1개만큼 존재하는 이유는 1-2. 에서 방향을 고려하지 않게 하기 위해서
3. 이 때, 각 점은 친구들이 단지 방문하거나 기존 점에서 이동하는 2가지 방법이 있다
=> 단지 방문하면 길이는 0
=> 기존 점에서 이동하면 마지막 거리값에서 플러스
4. 이제 구한 거리들이 실제로 가능한지 비교해본다.
=> 불가능한 거리라면 W+1을 answer에 apppend
=> 왜? -1을 append 하면 추후에 min을 쓰기 어려워진다
=> min을 왜써? 요구사항이 가장 작은 거리를 요구하기 때문
=> 이 거리들은 최대 W의 값을 가지므로 W+1의 값을 append
=> 이렇게 되면, min(answer) == W+1 일 때 -1을 출력 가능
'''
def solution(n, weak, dist):
    W = len(weak)
    weak += [w + n for w in weak]
    diff = [weak[idx] - weak[idx - 1] for idx in range(1, len(weak))]
    dist.sort(reverse=True)
    answer = []

    for st in range(W):
        stack, save = [[]], []
        for idx in range(st, W + st):
            while stack:
                lst = stack.pop()
                if len(lst) < len(dist):
                    save.append(lst + [0])
                if lst:
                    save.append(lst[:-1] + [lst[-1] + diff[idx]])
            stack, save = save, stack

        for s in stack:
            for a, b in zip(dist, sorted(s, reverse=True)):
                if a < b:
                    answer.append(W + 1)
                    break
            else:
                answer.append(len(s))

    return -1 if min(answer) == W + 1 else min(answer)

    return answer
'''
너무 어렵다. 5시간 정도 고민해서 풀었다 ㅠ__ㅠ
내 풀이가 모든 경우의 수를 따지므로 combination을 사용한 풀이와 원리는 비슷하다.
set을 사용한 풀이가 효율성이 좋던데 이해를 잘 못하겠다.
'''