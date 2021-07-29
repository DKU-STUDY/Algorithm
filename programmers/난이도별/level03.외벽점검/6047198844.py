import collections
import heapq

def solution(n, weak, dist):
    answer = 0
    graph = collections.defaultdict(list)
    N = len(weak)
    finders = []
    
    for i in dist:
        heapq.heappush(finders,-i)
    
    while finders and weak:
        finder = -heapq.heappop(finders)
        remove = tuple()
        remove_val = 0
        for i in weak:
            for j in weak:
                if i != j:
                    cost = min((j-i)%n,(i-j)%n)
                    if finder >= cost > remove_val:
                        remove = (i,j)
                        remove_val = cost
                        
        if remove_val == 0:
            return -1 if len(weak) > len(dist) else len(dist) - len(weak)
        else:
            i, j = remove
            weak.remove(i)
            weak.remove(j)
            print(i,j)
    
    
    return -1 if weak else len(dist) - len(finders)