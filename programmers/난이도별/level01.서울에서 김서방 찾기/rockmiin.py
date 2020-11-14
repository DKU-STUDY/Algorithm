def solution(seoul):
    answer=""
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            answer="김서방은 "+str(i)+"에 있다"
    return answer

print(
    solution(["Jane", "Kim"]),
    solution(["Jane", "Kim"])=="김서방은 1에 있다"
)

