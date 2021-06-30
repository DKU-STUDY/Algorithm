'''
https://programmers.co.kr/learn/courses/30/lessons/76503
모두 0으로 만들기
[풀이]
1. 각 노드끼리의 관계를 명시할 dictionary를 선언
2. bfs로 트리의 순서를 결정한다.
=> stack에서 pop된 원소는 자신과 연결되어있는 노드를 stack에 넣고 자신은 save에 넣는다.
=> 이 과정은 트리의 깊이순으로 save에 저장되는 과정이다.
=> 0번 인덱스를 이 트리의 노드로 간주했다.
=> 이 때, 담기는 구조는 [자신의 번호, 부모의 번호] 이다.
3. save에 담긴 노드들의 순서는 트리의 깊이가 가장 깊은 노드들부터 담겨있다.(pop 기준)
=> 따라서 이 노드들의 parent에게 자신의 가중치를 모두 전해준다.
=> 최종적으로 0번 루트 노드가 0을 가지면 가중치가 모두 상쇄된 것이고, 가지지 못하면 되지 못한것.
'''
from collections import defaultdict, deque
def solution(a, edges):
    size = len(a)
    dic = defaultdict(list)
    for st, ed in edges:
        dic[st].append(ed)
        dic[ed].append(st)

    answer = 0
    stack = deque([[0, None]])
    save = []

    while stack:
        idx, parent = stack.popleft()
        save.append([idx, parent])
        for value in dic[idx]:
            if value != parent:
                stack.append([value, idx])

    while len(save) > 1:
        idx, parent = save.pop()
        a[parent] += a[idx]
        answer += abs(a[idx])

    return answer if a[0] == 0 else -1
'''
처음에는 시간 초과를 해결할 수 없어서 결국 다른 풀이를 봤다.
https://velog.io/@ckstn0778/프로그래머스-76503번-가사-검색-O-1-Python
대부분의 풀이가 위 링크의 풀이와 대부분 비슷하다.
아마 내 풀이가 이 문제에 대해 블로그로 작성된 유일한 풀이가 아닐까?

저 풀이를 보면서 맘에 들지 않은 이유는,
실제 테스트에서
    import sys
    sys.setrecursionlimit(1000000)
이 부분을 모르면 어쨋든 해결하지 못하고, 이 부분은 python에서만 활용할 수 있기 때문이다.
단순히 js에서 combination 함수를 제공하는 라이브러리가 있고 없고의 문제가 아니다.
=> combination은 반복문으로 구현할 수 있지만 재귀깊이를 늘리는 것을 구현할 수 있는가?
그래서, 각 노드의 순서를 정의할 필요가 있었고 위와 같이 풀게 되었다.
'''