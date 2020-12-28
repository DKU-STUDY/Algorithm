def solution(s):
    ss = ""
    s = s.split(" ")
    for n in s:
        for i, st in enumerate(n):
            ss += st.lower() if i % 2 else st.upper()
        ss += " "
    return ss[:-1]


print(solution("try Hello world") == "TrY HeLlO WoRlD")
print(solution("Hello eVeryone") == "HeLlO EvErYoNe")
