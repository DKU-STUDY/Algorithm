def is_good_word(word) -> bool:
    stack = []
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return not bool(stack)

N = int(input())
res = 0
for _ in range(N):
    if is_good_word(input()):
        res += 1
print(res)