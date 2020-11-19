import itertools
def solution(numbers):
    permutation=[]
    for i in range(1,len(numbers)+1) :   #모든 경우의 수
        permutation+=list((map(int,map(''.join,itertools.permutations(numbers,i)))))

    permutation=set(permutation); permutation-=set(range(0,2))
    m=max(permutation)

    for i in range(2,int(m**0.5)+1) :  #에라토스테네스의 체
        permutation-=set(range(i*2,m+1,i))
    return len(permutation)
#100점

print(solution("011")==2)
print(solution("17")==3)
