def solution(s):
    slist = [s[0]]
    for x in s[1:]:
        if slist != [] and x == slist[-1]:
            slist.pop()
            continue
        slist.append(x)
    return int(slist == [])

print(solution("baabaa") == 1, solution("cdcd") == 0)