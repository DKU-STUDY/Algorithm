'''
https://leetcode.com/problems/redundant-connection/
684. Redundant Connection
그래프
'''
class Solution(object):
    def findRedundantConnection(self, edges):
        disjoint_set=[i for i in range(len(edges)+1)]
        def find_parent(i):
            while i!=disjoint_set[i]:
                i=disjoint_set[i]
            return i
        def union(a,b):
            source=find_parent(a)
            target=find_parent(b)
            disjoint_set[source]=target
            if source==target:
                return False
            return True
        for x,y in edges:
            if not union(x,y):
                return [x,y]
'''
개념 이해
https://bowbowbow.tistory.com/26
코드 참고
https://leetcode.com/problems/redundant-connection/discuss/1240764/almost-perfect-solution-simple-and-powerful-or-disjoint-set-union-or-python3

이 문제를 풀려면 Union-Find : Disjoint Set 이라는 개념을 알아야 한다.
DFS로도 풀수 있지만 시간 복잡도가 O(N) 이다.
Disjoint Set 은 시간 복잡도가 O(N) 이하 이다. (트리 구조가 연결리스트로 될 떄 O(N))
참고로 이 방법은 Union 시에 rank를 고려하지 않는 방법이다. (최적화도 고려하지 않았다)
여기서 rank와 최적화 까지 고려하면 머리가 더 아플듯...
'''