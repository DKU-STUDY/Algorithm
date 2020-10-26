def solution(skill, skill_trees):
    answer = 0
    len_skill = len(skill)
    for tree in skill_trees:
        order = []
        for i in range(len_skill):
            order.append(tree.find(skill[i])) #앞에꺼보다 크면 들어가게 변경 아래 싹 필요 없음

        for i in range(len_skill):
            if order[-1] == -1:
                order.pop()
            else:
                break

        if order[0] == -1:
            if sum(order) == -len(order): #선후수 스킬과 관계 없는 스킬만 찍을 경우
                answer += 1
        else:
            if order == sorted(order):
                answer += 1
    return answer
    
  print(solution("abc", ["adbic", "bcida","aicls"]), solution("abc", ["adbic", "bcida","aicls"]) == 1)
