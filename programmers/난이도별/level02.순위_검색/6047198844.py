#정확성 테스트 통과 효율성 테스트 통과 X
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
        *kind_info, score_info = info_.split()
        for kind in kind_info:
            kind_table[kind].add(idx)
        score_table[int(score_info)].add(idx)
    
    score_table = sorted(score_table.items(), key = lambda x:x[0])
    
    for query_ in query:
        *splited_query, score = query_.replace('-','').replace('and','').split()
        group_score, group = zip(*score_table)
        score_idx = bisect.bisect_left(group_score, int(score))
        
        res = set().union(*group[score_idx:])
        for q in splited_query:
            res &= kind_table[q]
        answer.append(len(res))
        
    return answer

#효율성 테스트 통과
import heapq
from bisect import bisect_left
from collections import defaultdict
from itertools import combinations

def solution(infos, queries):
    answer = []
    
    #타입에 따라 table에 담는다.
    table = defaultdict(list)
    
    #info를 타입과 점수로 분리한다.
    for info in infos:
        *info_type, info_score = info.split()
        #해당 타입으로 만들수있는 모든 경우의수에(쿼리도 나올수있는 경우의 수) 점수를 저장한다.
        for i in range(5):
            for c in combinations(info_type,i):
                table[''.join(c)].append(int(info_score))
    
    #bisect를 위해서 정렬.
    for v in table.values():
        v.sort()
    
    
    #쿼리로 검색한다.
    for query in queries:
        *query_type, query_score = query.replace('-','').replace('and','').split()
        query_type = ''.join(query_type)
        n = len(table[query_type]) - bisect_left(table[query_type], int(query_score))
        answer.append(n)
        
    return answer