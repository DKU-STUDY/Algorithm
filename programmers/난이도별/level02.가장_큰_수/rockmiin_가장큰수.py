def solution(num):
    num= list(map(str, num))
    slen= len(num)

    for i in range(slen):
        num[i]*=3
    # print(num)

    num.sort(reverse=True)
    for i in range(slen):
        num[i]=num[i][:len(num[i])//3]
    if num[0]=='0': return '0'
    return ''.join(num)


print(
    solution([6, 2, 10])
)
