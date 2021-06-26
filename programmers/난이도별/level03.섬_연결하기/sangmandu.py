'''
https://programmers.co.kr/learn/courses/30/lessons/42861
섬 연결하기
[풀이]
1. 크루스칼 알고리즘 사용 : https://it-garden.tistory.com/411
=> 최단 거리를 구하는 것이므로 cost가 작은 것부터 하나씩 선택
=> 만약 cycle이 된다면 거른다!
=> cycle이 아니라면 계속 선택
=> 언제까지? 점이 n개니까 간선은 n-1개이므로 이 때 까지
2. 초기에 각 점에 대한 소속 그룹은 자신으로 둔다.
=> 이후 각 간선에 대해 소속 그룹을 갱신한다.
=> 그리고 while문을 통해 각 점에 대한 소속 그룹을 탐색할 수 있도록 한다.
=> 보통은 함수로 많이 정의하는 것 같다. (간단한데도 불과하고?)
3. 소속 그룹이 같으면 cycle 이므로 pass 그렇지 않으면 cost 더해주기
'''
def solution(n, costs):
    costs.sort(key=lambda x: x[2], reverse=True)
    edge_amount = 0
    parent = list(range(n))
    answer = 0
    while edge_amount < n - 1:
        st, ed, cost = costs.pop()
        pst, ped = st, ed
        while parent[pst] != pst:
            pst = parent[pst]
        while parent[ped] != ped:
            ped = parent[ped]
        if pst == ped:
            continue
        edge_amount += 1
        parent[ped] = pst
        answer += cost
    return answer
'''
level3 들어서는 한시간 반씩은 푸는 것 같다...ㅠ
크루스칼 알고리즘. 간혹가다가 나오는 알고리즘.
그래프 문제를 탐욕법으로 풀 때 주로 등장하는 것 같다.
예전에도 한 번 크루스칼로 풀어봤는데, 까먹었다.
union-find 방식을 잘 기억해둘 것.
'''