def solution(clothes):

    list_kind=[]
    kind_count={}   #각 종류별 개수
    combination=1
    for r in clothes :
        list_kind.append(r[len(r)-1])

    for i in range(len(list_kind)) :
        for v in list_kind[i+1:] :
            if list_kind[i]==v :
                del list_kind[i]

    for r in clothes :
        for v in list_kind :
            if r[len(r)-1]==v :
                kind_count[v]=kind_count.get(v,0)+(len(r)-1)

    for i in kind_count.values() :
        combination*=(i+1)
    return combination-1
#점수 : 35.7점


cl=[['y','h','d'],['b','c'],['g','h'],['c','f','h'],['c','h']]
print(solution(cl))
