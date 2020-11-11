n= int(input())
arr=[]
for i in range(n):
    arr.append(input())

arr=set(arr)
answer=[]
for i in arr:
    answer.append([len(i), i]) # 인덱스를 단어의 길이인 배열 answer에 길이마다 저장
answer.sort()
# sort()는 앞 조건이 같으면 뒤 조건으로 정렬한다
for i in answer:
    print(i[1])
