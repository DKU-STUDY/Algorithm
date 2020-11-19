def solution(s):
    # 조건에 안맞는 것들을 바로 return 시키면 더 효율적인 코드가 됨.
    if len(s) != 4 and 6 :
        return False

    for i in s :
        if i not in "0123456789":
            return False
    return True

    print(solution("a234"))
