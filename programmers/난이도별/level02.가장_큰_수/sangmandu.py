'''
https://programmers.co.kr/learn/courses/30/lessons/42746#
가장 큰 수 : 주어진 숫자 리스트로 가장 큰 수 만들기
자리 수 길이만큼의 10의 제곱으로 나누어서 10보다 작은 소수 만들어 비교
'''

def solution(numbers):
    return str(int(''.join([j[0] for j in sorted([(str(i), i / (10 ** len(str(i))-1)) for i in numbers], key = lambda x : -x[1])])))

'''
와 근데 진짜
numbers.sort(key=lambda x: x*3, reverse=True)
이 방법은 정말로 참신하다.
'''