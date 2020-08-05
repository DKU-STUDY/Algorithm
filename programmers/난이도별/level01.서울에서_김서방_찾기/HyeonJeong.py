#방법1
'''
def solution(seoul):
    for m, n in enumerate(seoul):
        if "Kim" == n:
            return ("김서방은 %d에 있다" %m)
            # return "김서방은 {}에 있다".format(m)
'''

#방법2 : "Kim"이 리스트에서 한번만 존재하므로 index()사용
def solution(seoul):
    return "김서방은 %d에 있다" %index("Kim")
    # return "김서방은 {}에 있다".format(seoul.index("Kim"))

print(solution(["Jane","Kim"]) == "김서방은 1에 있다")