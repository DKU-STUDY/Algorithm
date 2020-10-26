def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        for i in range(len(skill) - 1):
            if tree.find(skill[i]) > tree.find(skill[i+1]):
                break
            else:
                if i == len(skill) - 2:
                    answer += 1
                continue
    return answer
    
  print(solution("abc", ["adbic", "bcida","aicls"]), solution("abc", ["adbic", "bcida","aicls"]) == 1)
