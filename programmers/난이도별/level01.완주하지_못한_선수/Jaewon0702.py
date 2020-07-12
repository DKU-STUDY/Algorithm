def solution(participant, completion):
    
    answer = ''

    for i in range(len(participant)) :

        if not participant[i] in completion:
            answer=participant[i]
    p_overlap=[]         #참가자 중복 이름 리스트
    c_overlap=[]         #완주자 중복 이름 리스트
    for i in range(len(participant)-1) :
        if participant[i] in participant[i+1:len(participant)] :
            p_overlap.append(participant[i])


    for i in range(len(completion)-1) :
        if completion[i] in completion[i+1:len(completion)] :
            c_overlap.append(completion[i])

    if len(p_overlap)!=0 :
        for i in range(len(p_overlap)) :
            if not p_overlap[i] in c_overlap :
                answer=p_overlap[i]


    
    return answer
    

