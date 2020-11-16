'''
https://programmers.co.kr/learn/courses/30/lessons/12950
행렬의 덧셈 : shape이 같은 리스트 더하기
zip 이용
'''

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer += [[j+k for j, k in zip(arr1[i], arr2[i])]]
    return answer

'''
실제로 구성해보고 싶던 코드는
def solution(arr1, arr2):
    return [[a + b for a, b in zip(c, d)] for c, d in zip(arr1, arr2) ]
'''