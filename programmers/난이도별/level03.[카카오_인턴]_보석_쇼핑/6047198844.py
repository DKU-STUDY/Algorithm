import collections

def solution(gems):
    target_num = len(set(gems))
    table = collections.defaultdict(int)
    cnt = 0
    res_cnt = 100001
    begin = 0
    answer = []
    
    for end, gem in enumerate(gems):
        #end값을 table에 추가한다.
        table[gem] += 1
        #추가한값이 새로운 값이라면, cnt를 증가시킨다.
        if table[gem] == 1:
            cnt += 1

        while table[gems[begin]] >= 2:
            table[gems[begin]] -= 1
            begin += 1
        
        if cnt == target_num and end - begin + 1 < res_cnt:
            answer = [begin + 1, end + 1]
            res_cnt = end - begin + 1
            
    
    return answer