def solution(s):
    return " ".join([ "".join([ st.lower() if i % 2 else st.upper() for i, st in enumerate(n)  ]) for n in s.split(" ")])


print(solution("try Hello world") == "TrY HeLlO WoRlD")
print(solution("Hello eVeryone") == "HeLlO EvErYoNe")
