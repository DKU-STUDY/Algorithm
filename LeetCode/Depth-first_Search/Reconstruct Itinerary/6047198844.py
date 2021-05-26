#경로가 최소 하나 존재한다 -> 어디로 가든 경로가 있다.
#다시풀기
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #변수이름
        graph = collections.defaultdict(list)
        
        #티켓을 sort하면 알파벳 순으로 리스트가 만들어짐.
        for depart, arrival in sorted(tickets): 
            graph[depart].append(arrival)
        
        result = []
        
        def dfs(depart):
            while graph[depart]:
                dfs(graph[depart].pop(0))
            result.append(depart)
        
        dfs("JFK")
        
        return result[::-1]
        
            
        '''
        #pre_itinerary = 이미 방문한 경로
        #누적 경로 / index로 저장.
        #ticket[0] -> 출발 / ticket[1] -> 도착
        def dfs(pre_itinerary: List):
            if len(pre_itinerary) == len(tickets):
                result_itinerary.append(pre_itinerary[:])
                return
            
            #pre_itinerary는 무조건 존재. 초기값은 JFK 출발.
            #가장 최근 경로
            last_itinerary = tickets[pre_itinerary[-1]]
            
            for idx, ticket in enumerate(tickets):
                #직전 도착지가 출발지와 같은 티켓이면서 이전에 방문하지 않았던 경로.
                if ticket[0] == last_itinerary[1] and not idx in pre_itinerary:
                    pre_itinerary.append(idx)
                    dfs(pre_itinerary)
                    pre_itinerary.pop()
        
        result_itinerary = []
        
        for idx, ticket in enumerate(tickets):
            if ticket[0] == "JFK":
                dfs([idx])
        
        #출발지점인 "JFK"를 붙여줘야할것임.
        result_itinerary = [["JFK"] + [tickets[idx][1] for idx in result] for result in result_itinerary]
        #result_itinerary에는 도착경로가 저장되어있음.
        return min(result_itinerary)
    
    #실수한 부분. 같은 간선이 중복된다면?
    #TLE -> 다시 접근        
        '''
