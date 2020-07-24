def solution(bridge_length, weight, truck_weights):
    count=len(truck_weights)
    time=[0]*count ; passed=[]; passing=[]
    i=0 ; j=-1

    truck_weights=truck_weights[::-1]

    while(len(passed)<count) :

        if (len(truck_weights)>0) and (sum(passing)+truck_weights[-1]) <= weight :
            passing.append(truck_weights.pop())
            j+=1

        time[:j+1] = [time[v]+1 for v in range(j+1)]  #각 트럭이 다리에 오르고 몇 초가 지났는지 알 수 있다.

        if time[i]==bridge_length :
            passed.append(passing.pop(0))   #Ln : 17
            i+=1
    return time[0]+1

'''Ln : 17= passed.append(passing[0])
            passing = passing[1:]    과 같이 바꿀 수 있다.'''
    
#https://leedakyeong.tistory.com/entry/프로그래머스-다리를-지나는-트럭-in-python를 참고하였다.
                
        
 
                         
    






