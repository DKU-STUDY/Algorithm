def solution(lottos, win_nums):
    cnt = 0
    for l in lottos:
        cnt += l in win_nums
        
    high = min(6,7-cnt-lottos.count(0))
    low = min(6,7-cnt)
    
    return [high,low]