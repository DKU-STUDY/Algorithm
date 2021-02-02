
def solution(user_id, banned_id):
    global answer
    answer= 0
    res= []
    ban_list= [[] for _ in range(len(banned_id))]
    for ban in range(len(banned_id)):
        for user in user_id:
            if len(banned_id[ban])==len(user):
                cnt= 0
                for i in range(len(user)):
                    if banned_id[ban][i] == '*': cnt+=1; continue
                    elif banned_id[ban][i] != user[i]: break;
                    cnt+=1
                if cnt== len(banned_id[ban]):
                    ban_list[ban].append(user)

    def select(res_list, cnt):
        global answer

        if cnt == len(ban_list):
            if sorted(res_list) not in res:
                res.append(sorted(res_list))
                answer+=1
                print("res_list", res_list);
            return
        for i in range(len(ban_list[cnt])):
            if not ban_list[cnt][i] in res_list:
                res_list.append(ban_list[cnt][i])
                select(res_list, cnt+1)
                res_list.pop(-1)

    select([], 0)
    # print(res)
    
    return answer

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
         ["fr*d*", "abc1**"])

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
         ["*rodo", "*rodo", "******"])

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
         ["fr*d*", "*rodo", "******", "******"])