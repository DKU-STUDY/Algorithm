# 출처 https://programmers.co.kr/learn/courses/30/lessons/49993
# skill 선행 스킬 순서 문자열, (1이상 26이하)
# skill_trees 검사해봐야할 스킬트리 문자열(2이상 26이하)들의 리스트(1이상 20이하)
# 선후수를 만족하는 스킬트리의 갯수 return


def solution(skill, skill_trees):
    answer = 0
    len_skill = len(skill)
    for tree in skill_trees:
        order = []
        for i in range(len_skill):# order 리스트에 skill의 index를 찍어줌
            order.append(tree.find(skill[i]))

        for i in range(len_skill):# ex) [3, 5, 1, -1, -1] => [3, 5, 1]로 만들어줌
            if order[-1] == -1:
                order.pop()
            else:
                break

        if order != []:
            if order[0] == -1:               # 첫번째 스킬 안찍으면 뒷 스킬은 하나도 찍으면 안됨
                if sum(order) == -len(order):# 의도 : order의 모든 요소가 -1 일때
                    answer += 1
            else:
                if order == sorted(order):   # 모두 -1이 아니라면 순서대로 찍혀있어야됨
                    answer += 1
        else:                                # skill에 있는 스킬 하나도 안찍었을때
            answer += 1                      # 윗부분(line23)이랑 겹치는데 이상함 둘중에 하나라도 빠지면 안됨

    return answer
    
print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]), \
      solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]) == 2)

print(solution("abc", ["adbic", "ajrgp", "bcida","aicls", "bdgs", "abc","qwer"]), \
      solution("abc", ["adbic", "ajrgp", "bcida","aicls", "bdgs", "abc","qwer"]) == 4)
# my test case
