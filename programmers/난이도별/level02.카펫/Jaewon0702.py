import math
def solution(brown, yellow) :
    row=int(( 2 + brown/2 + math.sqrt( (2 + brown/2)**2 - 4*(brown + yellow))) /2) #근의 공식
    return[row,int (brown/2- row + 2)]

#100점
print(solution(10,2)==[4,3])
print(solution(8,1)==[3,3])
print(solution(24,24)==[8,6])



