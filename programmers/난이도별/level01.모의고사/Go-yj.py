'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/42840
문제 : 모의고사
i%len(student)로 나머지를 이용해 검사하였습니다.
max값을 가진 index를 return하여 답을 구하였습니다.
'''

def solution(answers):
    answer = [0,0,0]
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)) :
        if answers[i] == student1[i%len(student1)] : answer[0] += 1
        if answers[i] == student2[i%len(student2)] : answer[1] += 1
        if answers[i] == student3[i%len(student3)] : answer[2] += 1
    return [x+1 for x in range(len(answer)) if answer[x]==max(answer)]
