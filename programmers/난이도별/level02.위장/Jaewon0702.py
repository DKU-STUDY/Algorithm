def solution(clothes):
    kind_count={}
    for v in clothes :
        key=v[len(v)-1]
        kind_count[key]=kind_count.get(key,0)+1
    combination=1
    for i in kind_count.values() :
        combination*=(i+1)
    return combination-1
#점수 : 100점


cl=[['y','d'],['b','c'],['g','h'],['c','h'],['c','h']]
print(solution(cl))
