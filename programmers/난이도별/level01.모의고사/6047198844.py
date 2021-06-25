import collections

def solution(answers):    
    give_up_maths = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    cnts = []
    
    for idx, answer in enumerate(answers):
        for n in range(0,3):
            if give_up_maths[n][idx % len(give_up_maths[n])] == answer:
                cnts.append(n+1)
    cnts = collections.Counter(cnts).most_common()
    return sorted([i for i, cnt in cnts if cnt == cnts[0][1]])