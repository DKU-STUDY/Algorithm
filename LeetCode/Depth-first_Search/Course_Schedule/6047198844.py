class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        for pre_course, course in prerequisites:
            graph[pre_course].append(course)
        
        traced = set()
        visited = set()
        
        def dfs(precourse):
            if precourse in traced:
                return False
            
            if precourse in visited:
                return True
            
            traced.add(precourse)
            for course in graph[precourse]:
                if not dfs(course):
                    return False
            #for문을 나와서 제거해야한다. 모든 재귀 호출은 traced에 해당 precourse가 존재해야한다.
            traced.remove(precourse)
            visited.add(precourse)
            
            return True
        
        for i in list(graph):
            if not dfs(i):
                return False
        
        return True