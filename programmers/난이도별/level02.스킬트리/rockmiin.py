def solution(skill, skill_trees):
    ans = 0
    skill = list(skill)
    for tree in skill_trees:
        tmp= []
        for s in tree:
            if s in skill:
                tmp.append(s)
        if tmp == []:
            ans += 1; continue

        idx = 0
        for i in range(len(tmp)):
            if tmp[i] == skill[idx] and idx < len(skill):
                idx += 1
            elif idx < len(skill) - 1 and tmp[i] in skill[idx + 1:]:
                break;
        else:
            ans += 1

    return ans
