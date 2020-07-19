# 방법1
def solution(n):
    answer = ''
    word1 = '수'
    word2 = '박'
    for i in range(n) :
        if i % 2 == 0 :
            answer += word1
        else :
            answer += word2
    return answer

# 방법2
def solution(n):
    answer = '수박' * (n//2) + '수' * (n % 2)
    return answer

print("n이 3일때 : " + solution(3))