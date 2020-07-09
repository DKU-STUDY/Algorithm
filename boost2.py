def solution(arrayA, arrayB):
    a=arrayA.copy()
    b=arrayB.copy()

    a=sorted(a); b=sorted(b)
    overlap(a); overlap(b)

    #sum 구현 A가 base
    sum=sorted(a.copy()+b.copy()); overlap(sum)
    complement=comp(a.copy(), b.copy())
    intersect=inter(sorted(a.copy()+b.copy()))
    ret=[len(a), len(b), len(sum), len(complement), len(intersect)]
    return ret

def overlap(array):
    idx=[]; cnt=0
    for i in range(len(array)-1):
        if(array[i]==array[i+1]):
            idx.append(i)
    for i in idx:
        array.pop(int(i)-cnt)
        cnt+=1

def comp(a, b):
    idx=[]; cnt=0
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i]==b[j]):
                idx.append(i)
    for i in idx:
        a.pop(int(i)-cnt)
        cnt+=1
    return a

def inter(array):
    idx = [];
    for i in range(len(array) - 1):
        if (array[i] == array[i + 1]):
            idx.append(array[i])
    return idx


if __name__=="__main__":
    A=[2,3,4,3,5]
    B=[1,6,7]
    print(solution(A, B))

