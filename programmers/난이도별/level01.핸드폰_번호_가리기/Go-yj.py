'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12948
문제 : 핸드폰 번호 가리기
뒤 4글자를 제외한 나머지 *을 for문으로 넣은 후, 뒤 네글자 추가하여
각각 나누어진 문자열을 하나로 합쳤습니다.
다른 사람 코드를 보니 문자열 곱셈을 하면 되는데 바보처럼 했네요 ㅠ
[메모메모]
'*'*(len(phone_number)-4)+phone_number[-4:]
'''

def solution(phone_number):
    answer = ''
    answer = ['*' for x in range(len(phone_number)-4)]
    back = phone_number[-4:]
    answer += back
    answer = ''.join(answer)
    return answer
