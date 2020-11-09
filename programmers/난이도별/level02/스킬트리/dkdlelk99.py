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

        if order == []:
            answer += 1
        else:
            if order[0] == -1:
                continue
            elif order == sorted(order):
                answer += 1

    return answer
    
print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]), \
      solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]) == 2)

print(solution("abc", ["adbic", "ajrgp", "bcida","aicls", "bdgs", "abc","qwer"]), \
      solution("abc", ["adbic", "ajrgp", "bcida","aicls", "bdgs", "abc","qwer"]) == 4)
# my test case
