# 방법 1
'''
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
'''

# 방법 2(더 간단하고 효율적인 코드로)
def solution(n):
    return '수박' * (n//2) + '수' * (n % 2)
    
print("n이 3일때 : " + solution(3))
