def solution(s):
    return "".join(sorted(list(s), reverse=True))

print(
    solution("Zcbdefg")=="gfedcbZ"
)
