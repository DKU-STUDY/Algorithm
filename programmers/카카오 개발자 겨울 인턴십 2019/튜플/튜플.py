
def solution(s):
    # },{ 기준으로 나눠준 다음에 앞에 {{, }}를 떼주어서 list로 만들었다.

    arr= s.split('},{')
    arr[0]= arr[0][2:]
    arr[-1]= arr[-1][:-2]
    res= []

    for i in range(len(arr)):
        arr[i]= list(map(int, arr[i].split(',')))
        # print(arr)
    # 정렬을 리스트의 길이 순서대로 해주어 문자열의 길이가 작은 것부터 값을 추가해 준 뒤 반환

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