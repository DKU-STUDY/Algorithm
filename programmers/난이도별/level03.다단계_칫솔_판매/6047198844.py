def dfs(enroll_referral, seller, credit):
    if seller == "-":
        dict[seller] = credit + dict.get(seller, 0)
        return

    dict[seller] = dict.get(seller, 0) + credit - (credit // 10)
    seller = enroll_referral[seller]

    dfs(enroll_referral, seller, credit // 10)


def solution(enroll, referral, seller, amount):
    answer = []
    global dict
    dict = {}
    
    enroll_referral = {}
    
    for idx in range(len(enroll)):
        enroll_referral[enroll[idx]] = referral[idx]
    
    for idx in range(len(amount)):
        dfs(enroll_referral, seller[idx], amount[idx]*100)
    
    return [dict.get(i,0) for i in enroll]