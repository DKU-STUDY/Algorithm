def solution(numbers) :
    biggest=''
    sorted_v=[]
    for v in numbers :
        sorted_v.append(str(v)*3)
    sorted_v.sort(reverse=True)
    for v in sorted_v :
        biggest+=v[:int(len(v)/3)]
    if biggest[0]=='0' :
        return '0'

    return biggest
#kdlelk99님의 코드를 참고하였다. 6줄을 좀 더 간단한 코드로 줄였다.
#100점

            
        
        


    
            

    
            
        
