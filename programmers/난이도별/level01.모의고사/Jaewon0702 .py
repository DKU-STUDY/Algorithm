def solution(answers):
    math_haters=[[1,2,3,4,5],
                 [2,1,2,3,2,4,2,5],
                 [3,3,1,1,2,2,4,4,5,5]]
    scores=[0]*len(math_haters)

    for i,answer in enumerate(answers) :
        for k,marking in enumerate(math_haters) :
            if answer==marking[i%len(marking)] :
                scores[k]+=1
    return [i+1 for i,score in enumerate(scores) if max(scores)==score]

#100점
print(solution([1,2,3,4,5])==[1])
print(solution([1,3,2,4,2])==[1,2,3])
