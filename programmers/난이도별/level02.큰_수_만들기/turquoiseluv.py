'''
https://programmers.co.kr/learn/courses/30/lessons/42883

매번 비교하려니까 런타임 오류가 발생했고,
    while k > 0 and len(ans) < len(number)-k:
        if number[target] == max(number[target:target+k+1]):
            ans += number[target]
기존의 배열의 순서가 바뀌지 않는 점을 이용하여, que에 들어오는 숫자들만 보며, 최적인지 판단할 수 있었다.

1) que를 만들고, number에서 하나씩 값(num)을 넘긴다. append(pop())
2) 이떄, 넘기는 값이 que의 맨 마지막 값(que[-1])보다 작으면, 더 큰 값이 나올 때까지 que[-1]을 버리고 반복
    2-1) que = ['9']는 한자리 수로 더 큰 값을 가질 수 없기 때문에, que.pop()의 방지턱이 된다.
3) 해당 과정에서 버릴 때마다 제거해야 하는 개수 k값에서 1씩 감소
4) while문이 완료 후, 남은 number 배열을 que애 더해준다.
5) k가 남은 경우(number==null로 탈출), 이미 정렬이 완료된 que에서 남은 k만큼 뒤에서 제거해준다.
'''

number = '4177252841'
k = 4

def solution(number, k):
    number = list(number[::-1])
    que = ['9']
    while number and k > 0:
        num = number.pop()
        while que[-1] < num and k > 0:
            que.pop()
            k -= 1
        que.append(num)
    que += number[::-1]
    if k != 0:
        que = que[:-k]
    return ''.join(que[1:])

print(solution(number, k))
