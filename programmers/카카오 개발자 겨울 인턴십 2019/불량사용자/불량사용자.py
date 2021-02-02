


def solution(user_id, banned_id):
    global answer
    answer= 0
    res= []
    ban_list= [[] for _ in range(len(banned_id))]
    
    # user_id와 banned_id를 매개변수로 받아서 banned_id 기준으로 길이가 같은 user_id 중에서 *인 문자를 제외하고 동일하다면 ban_list에 user_id를 넣어준다.
    # banned_id의 index에 맞는 user_id가 ban_list에 들어가게 된다. 

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

    # ban_list에서 index마다 하나씩 뽑아서 조합을 구성해준다.
    # 재귀 형태로 구현을 할 것이며 이때 중요한 점은 이 전에 뽑아준 user_id가 중복해서 들어가는 경우는 제외되도록 구현을 해줌.
    def select(res_list, cnt):
        global answer

        if cnt == len(ban_list):
            if sorted(res_list) not in res:
                res.append(sorted(res_list))
                answer+=1
                # print("res_list", res_list);
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