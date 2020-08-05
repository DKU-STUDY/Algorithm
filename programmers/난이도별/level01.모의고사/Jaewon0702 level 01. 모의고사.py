def solution(answers):
    math_hater1=[1,2,3,4,5]
    math_hater2=[2,1,2,3,2,4,2,5]
    math_hater3=[3,3,1,1,2,2,4,4,5,5]
    scores=[0]*3; First_place=[]

    for i,answer in enumerate(answers) :
        if answer==math_hater1[i%len(math_hater1)] :
            scores[0]+=1

        if answer==math_hater2[i%len(math_hater2)] :
            scores[1]+=1

        if answer==math_hater3[i%len(math_hater3)] :
            scores[2]+=1

    for i,score in enumerate(scores) :
        if max(scores)==score :
            First_place.append(i+1)
    return First_place

print(solution([1,2,3,4,5])==[1])
print(solution([1,3,2,4,2])==[1,2,3])
