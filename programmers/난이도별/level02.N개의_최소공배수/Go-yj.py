'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12953
문제 : N개의 최소공배수
예전에 리뷰에서 최소공배수는 (두 수의 곱 // 최대공약수)라고 알려줬었는데
새까맣게 잊어버리고 뻘짓 했습니다..ㆆ_ㆆ
다른 사람들 풀이를 보니 gcd로 바로 약수를 구할수도 있더라구요!!!
[메모메모]
1. from math import gcd
2. a*b // gcd(a,b)
앞으로 최소공배수는 더 편하게 풀수 있도록 연습해야겠어요
'''
def solution(arr):
    for i in range(len(arr)-1) :
        temp_lcm = lcm(arr[i],arr[i+1])
        arr[i+1] = temp_lcm
    return arr[-1]

def lcm(a,b) :
    if b%a==0 : return b
    gcd = 1
    for i in range(min(a,b),0,-1) :
        if a%i==0 and b%i==0 :
            gcd = i
            break
    return gcd*(a//gcd)*(b//gcd)
