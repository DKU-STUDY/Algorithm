import collections

def solution(gems):
    target_num = len(set(gems))
    table = collections.defaultdict(int)
    cnt = 0
    begin = 0
    answer = [0, 100001]
    
    for end, gem in enumerate(gems):
        #end값을 table에 추가한다.
        table[gem] += 1
        #추가한값이 새로운 값이라면, cnt를 증가시킨다.
        if table[gem] == 1:
            cnt += 1

        #맨 앞에 있는 값이 두개 이상의 값을 가지고 있다면 begin을 증가시켜 윈도우를 줄인다
        #물론 윈도우를 줄이면서 해당 값을 감소시킨다
        while table[gems[begin]] >= 2:
            table[gems[begin]] -= 1
            begin += 1
        
        if cnt == target_num and end - begin < answer[1] - answer[0]:
            answer = [begin + 1, end + 1]
    
    return answer