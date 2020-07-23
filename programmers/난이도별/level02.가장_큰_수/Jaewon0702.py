def solution(numbers) :
    biggest=''
    sorted_v=[]
    sorted_v = sorted([ str(v) * 3 for v in numbers ], reverse=True)   
    sorted_v.sort(reverse=True)
    for v in sorted_v :
        biggest+=v[:int(len(v)/3)]
    if biggest[0]=='0' :
        return '0'

    return biggest
#kdlelk99님의 코드를 참고하였다. 
#100점

            
        
        


    
            

    
            
        
