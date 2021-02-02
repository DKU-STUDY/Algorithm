
def solution(s):

    arr= s.split('},{')
    arr[0]= arr[0][2:]
    arr[-1]= arr[-1][:-2]
    res= []

    for i in range(len(arr)):
        arr[i]= list(map(int, arr[i].split(',')))
        # print(arr)
    arr.sort(key= len)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if not arr[i][j] in res:
                res.append(arr[i][j])
    # print(res)
    return res



solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
solution("{{20,111},{111}}")
solution("{{123}}")
solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")