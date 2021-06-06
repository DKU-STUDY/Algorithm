class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #예외처리
        if n <= 1:
            return [0]
            
        #graph를 만든다.
        graph = defaultdict(deque)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        #하나만 연결되있으면 leaf이다.
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)
                
        
        #leaves의 길이가 2이하일때까지 leaf들을 다 때낸다.
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                #leaf를 때낸다. leaf와 연결된 이웃을 없애고 자신도 없앤다.
                neighbor = graph[leaf].popleft()
                graph[neighbor].remove(leaf)
                
                #때낸후 이웃도 leaf가 될수있다.
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        return leaves