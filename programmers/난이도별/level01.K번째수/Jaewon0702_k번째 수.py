def solution(array, commands):
    cutter=[] ; answer=[]
    for v in commands :
        cutter=sorted(array[v[0]-1:v[1]]) 
        answer.append(p[v[2]-1])
    return answer

#점수 : 100점



