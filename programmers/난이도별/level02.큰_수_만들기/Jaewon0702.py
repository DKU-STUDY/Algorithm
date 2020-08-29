def solution(number, k):
    stack = []
    for num in number:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return "".join(stack)


# 100점
# https://train-validation-test.tistory.com/entry를 참고하였음.

print(solution("1924", 2) == "94")
print(solution("1231234", 3) == "3234")
print(solution("4177252841", 4) == "775841")
print(solution("100000", 2) == "1000")
