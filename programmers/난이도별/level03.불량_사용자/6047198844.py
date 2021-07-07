import re
import collections

#경우의 수만 계산하면됨.

limited_ids = set()

def dfs(idx, matched, banned_ids,res):
    if idx == len(banned_ids):
        limited_ids.add(''.join(sorted(list(res))))
        return
    
    for user_id in matched[banned_ids[idx]]:
        if user_id not in res:
            res.add(user_id)
            dfs(idx+1,matched, banned_ids,res)
            res.remove(user_id)
    return
    
        
def solution(user_ids, banned_ids):
    answer = 0
    matched = collections.defaultdict(set)
    
    banned_ids = list(map(lambda banned_id: banned_id.replace('*','.'), banned_ids))
    
    #banned_id에 맞는 user_id를 배분.
    for banned_id in banned_ids:
        cnt = 0
        for user_id in user_ids:
            if len(banned_id) == len(user_id) and re.search(banned_id, user_id):
                matched[banned_id].add(user_id)
                
    dfs(0, matched, banned_ids, set())
    return len(limited_ids)