'''
https://programmers.co.kr/learn/courses/30/lessons/77886
110 옮기기
[풀이]
1. 110을 s에서 모두 빼낸다.
=> 이후, 110을 특정 위치에 넣을것임
=> 110이 몇개가 있는지 총 개수를 센다.
2. 110을 미리 빼내도 문제가 없는 것인가?
=> 그렇다. 110은 앞뒤로 대칭이 아니다. 문제되지 않음
=> 만약 111이었다면 문제가 될 수 있다.
=> 111을 다 빼고 다시 넣어도 새로운 111이 생길 수 있기 때문
3. 이후 뒤에서부터 s를 세서 0을 만나면 바로 그 뒤에 110을 추가한다.
=> 왜?
=> 110은 사전순으로 뒤에서 두번째의 수이다.
=> 뒤에서 첫번째의 수는 111
=> 따라서 111 보다는 앞에있어야 한다.
=> 근데 0을 만나면 왜 바로 그 뒤에 추가해? 0전에 111이 있을수도 있잖아
=> 가정과 상충한다. 가정 : 이미 110을 다 뽑았음. 0전에 11이 있을 수가 없다.
=> 그 외에 수들은 0 00 000 10 100 이 있을 수 있다.
=> 이 수들은 모두 110 보다 사전순으로 앞에 오는 수.
=> 따라서 0을 발견하면 바로 그 뒤에 추가한다. => else문
=> if는 110이 존재하지 않을 때의 예외
=> elif는 110을 다 뺏더니 남은 수가 없을 때의 예외
'''
def solution(s):
    results = []
    for num in s:
        stack = ''
        ooz = 0
        for n in num:
            stack += n
            if len(stack) > 2 and stack[-3:] == "110":
                stack = stack[:-3]
                ooz += 1

        add = '110' * ooz
        if ooz == 0:
            results.append(stack)
        elif len(stack) == 0:
            results.append(add)
        else:
            for idx in range(len(stack) - 1, -1, -1):
                if stack[idx] == "0":
                    break
            else:
                idx -= 1
            results.append(stack[:idx + 1] + add + stack[idx + 1:])

    return results
'''
굉장히 어려운 문제.
https://prgms.tistory.com/57?category=882795를 참고했다.
'''