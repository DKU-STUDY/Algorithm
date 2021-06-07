'''
https://programmers.co.kr/learn/courses/30/lessons/77885
2개 이하로 다른 비트
비트 조작
'''
def solution(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number + 1)
            continue
        bit = '0' + format(number, 'b')
        for idx, val in enumerate(bit[::-1], 1):
            if val == "0":
                break
        idx = len(bit) - idx
        bit = bit[:idx] + bit[idx + 1] + bit[idx] + bit[idx + 2:]
        result.append(int(bit, 2))

    return result
'''
짝수일 경우는 바로 +1 한 수가 되고
홀수일 경우는
1. 제일 오른쪽 자리부터
2. 1이 연속으로 나오다 끝난 자리를 찾고
3. 이 자리와 그 왼쪽에 있는 0을 바꾼 수가 된다.

10진수를 2진수로 변환 : format(num, 'b')
2진수를 10진수로 변환 : int(str, 2)

처음에는 아래 코드처럼 접근했는데, 테스트 10, 11에서 시간초과.
컴퓨터 식 풀이가 아니라 규칙을 찾아야 되는 문제라고 생각이 드는 시점

def solution(numbers):
    result = []
    for number in numbers:
        n = number
        number_str = format(number, 'b')
        while True:
            n += 1
            n_str = format(n, 'b')
            if len(n_str) > len(number_str):
                number_str = '0'*(len(n_str)-len(number_str)) + number_str
            if [int(a!=b) for a, b in zip(n_str, number_str)].count(1) <= 2:
                result.append(n)
                break
    return result
    
다음 코드는 보수를 이용한 코드.
2의 보수와 2를 xor하면 1이 연속되다가 끊기는 부분의 인덱스를 얻을 수 있는 것 같다
def solution(numbers):
    answer = []
    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val+1)) >> 2) +val +1)

    return answer

'''