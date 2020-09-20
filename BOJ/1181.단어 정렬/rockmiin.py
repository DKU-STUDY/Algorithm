n= int(input())
arr=[]
for i in range(n):
    arr.append(input())

arr=set(arr)
answer=[[] for _ in range(len(arr)+1)]
for i in arr:
    answer[len(i)].append(i) # 인덱스를 단어의 길이인 배열 answer에 길이마다 저장
# print(answer)
for i in answer:
    if i: # answer값 중 []처럼 빈 곳이 있어서 값이 있을때만 정렬
        i=sorted(i)
        for j in i:
            print(j)