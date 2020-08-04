def solution(progresses, speeds):
    days=0; days_list=[]; publish=[]

    for i,p in enumerate(progresses) :   #대신 speeds를 사용해도 된다.
        while (p+speeds[i]*days<100) :
            days+=1
        days_list.append(days); days=0

    long=days_list[0]; length=len(days_list)

    for i,d in enumerate(days_list) :    #이 이후로 dkdlelk99님의 코드를 참고하였다.
        if long<d :
            long=d ; publish.append(days); days=1
        else :
            days+=1

        if i== length-1 :
            publish.append(days)
            
    return publish

p=[93,30,55]; s=[1,30,5]
print(solution(p,s)==[2,1])


#100점


        
    
