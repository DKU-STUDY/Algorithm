import collections
import re
import bisect
from functools import reduce

def solution(info, query):
    answer = []
    #info를 기준으로 dictionary를 만든다.
    
    kind_table = collections.defaultdict(set)
    score_table = collections.defaultdict(set)
    
    #info를 나누어 테이블에 담는다.
    for idx, info_ in enumerate(info):
        splited_info = info_.split()
        for kind in splited_info[:-1]:
            kind_table[kind].add(idx)
        score_table[int(splited_info[-1])].add(idx)
    
    score_table = sorted(score_table.items(), key = lambda x:x[0])
    
    for query_ in query:
        splited_query = query_.replace('and',' ').split()
        score = int(splited_query[-1])
        
        sc, gr = zip(*score_table)
        
        s = bisect.bisect_left(sc, score)
        res = set().union(*gr[s:])
        
        for q in splited_query[:-1]:
            if q == '-':
                continue
            res &= kind_table[q]
        answer.append(len(res))
        
    return answer