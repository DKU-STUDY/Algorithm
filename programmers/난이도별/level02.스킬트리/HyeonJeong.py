def solution(skill, skill_trees):
    answer = 0
    slist = [""]*len(skill_trees)
    for i, x in enumerate(skill_trees):
        for y in x:
            if y in skill:
                slist[i] += y
    for j in slist:
        if skill.find(j) == 0:
            answer += 1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])== 2)
