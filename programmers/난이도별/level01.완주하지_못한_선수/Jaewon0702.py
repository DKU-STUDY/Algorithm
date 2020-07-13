def solution(participant, completion):
    answer=''  
    participant.sort()
    completion.sort()
    completion.append('')
    for i in range(len(completion)) :
        if participant[i]!=completion[i] :
            answer=participant[i]
            break   
    return answer
    

