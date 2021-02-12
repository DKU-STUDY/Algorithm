'''
https://programmers.co.kr/learn/courses/30/lessons/42895
N으로 표현 : 1부터 9의 숫자 중 하나인 n을 최소로 사용하여 임의의 수 제작
총 6가지의 수로 나누었다.
1) 사칙연산 4가지와 자신을 자신으로 나눈 수 1에 대한 +, - 연산 2가지(*, // 연산은 의미가 없다)
2) 이 문제의 골치는 사칙연산 외에도 55, 555 같은 연결연산도 허용한다는 것.
따라서 반복문을 통해 cnt만큼을 비교.
'''


def solution(N, number):
    num = str(N)
    nums = [0] + [int(num * i) for i in range(1, 9)]

    def cal(val, cnt):
        if cnt > 8: return 9
        if val == number: return cnt

        exp = [9]
        for i in range(1, 9 - cnt):
            exp.append(cal(val + nums[i], cnt + i))
            exp.append(cal(val - nums[i], cnt + i))
            exp.append(cal(val * nums[i], cnt + i))
            exp.append(cal(val // nums[i], cnt + i))

        return min(
            min(exp),
            cal(val + 1, cnt + 2),
            cal(val - 1, cnt + 2),
        )

    answer = cal(0, 0)
    return answer if answer < 9 else -1


'''
몇몇 사람은 부분집합? 관계를 이용해서 풀던데 이해하기 귀찮아서 패스..
'''