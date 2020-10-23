'''
https://programmers.co.kr/learn/courses/30/lessons/12921
소수 찾기 : n 까지의 소수 찾기
제곱근까지 탐색
'''

def solution(n):
    if n == 2: return 1
    answer = 1
    for i in range(3, n+1, 2):
        prime = True
        for j in range(3, int(i**0.5)+1):
            if i % j == 0:
                prime = not prime
                break
        if prime : answer += 1
    return answer
'''
테스트 1 〉	통과 (3042.69ms, 10.3MB)
테스트 2 〉	통과 (2873.18ms, 10.2MB)
테스트 3 〉	통과 (2995.77ms, 10.4MB)
테스트 4 〉	통과 (2966.03ms, 10.5MB)
'''
'''
소수 찾기를 할 때는 에라토스테네스의 체를 사용하면 다음과 같이 풀이할 수 있다.
메모리 사용과 속도를 tradeoff 해서 10배가 적용됨
def solution(n):
    num=set(range(2,n+1))
    for i in range(2,int(n**0.5)+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
    
테스트 1 〉	통과 (279.54ms, 117MB)
테스트 2 〉	통과 (271.73ms, 115MB)
테스트 3 〉	통과 (270.61ms, 116MB)
테스트 4 〉	통과 (274.70ms, 116MB)
'''
'''
제곱근 방식을 적용했지만 간단한 코드
all을 이용해 하나라도 n % i == 0이 나오면 false로 간주했다
def is_prime(n):
    return all([(n%j) for j in range(2, int(n**0.5)+1)]) and n>1
'''