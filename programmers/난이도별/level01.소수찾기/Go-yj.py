'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12921
문제 : 소수 찾기
처음에는 본인을 제외한 2 이상의 수로 나누어 떨어지는 것이 없는지 전부 계산하여 소수를 찾았습니다.
그러면 효율성 테스트가 0점이 나오더라구요.
소수를 더 빠르게 구하는 방법으로 에라토스테네의 체를 알게 되었고
배열에 소수를 찾을 범위를 넣고, 배수를 없애는 방법으로 문제를 풀었습니다.
'''

def solution(n):
    answer = 0
    n_array = [i for i in range(n+1)]
    for i in range(2,n+1) :
        if n_array[i] :
            for j in range(i*2,n+1,i) :
                n_array[j] = False
    for i in range(2,n+1) :
        if n_array[i] : answer += 1
    return answer
