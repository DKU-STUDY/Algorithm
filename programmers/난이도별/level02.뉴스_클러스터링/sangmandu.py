'''
https://programmers.co.kr/learn/courses/30/lessons/17677
뉴스 클러스터링
두 글자씩 끊고 lower와 isalpha 검사. 이후, union, intersection 구하기
'''


def solution(str1, str2):
    str1, str2 = [str1[i] + str1[i + 1] for i in range(len(str1) - 1)], [str2[i] + str2[i + 1] for i in
                                                                         range(len(str2) - 1)]
    str1, str2 = [i.lower() for i in str1 if i.isalpha()], [i.lower() for i in str2 if i.isalpha()]
    union = str1 + str2
    intersection = []
    for i in str1:
        if i in str2:
            intersection.append(i)
            str2.remove(i)
    for i in intersection:
        if i in union:
            union.remove(i)
    return int(len(intersection) / len(union) * 65536) if len(union) else 65536


'''     
'''