import collections
    
def solution(tickets):
    answer = []
    graph = collections.defaultdict(list)
    
    for ticket in tickets:
        departure, arrival = ticket
        graph[departure].append(arrival)
    
    for edges in graph.values():
        edges.sort()
    
    def dfs(departure):
        while graph[departure]:
            arrival = graph[departure].pop(0)
            dfs(arrival)
        answer.append(departure)
    
    dfs("ICN")
    
    return answer[::-1]