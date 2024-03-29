# 문제
# 음료들은 정수로 표현되는 고유 번호를 가지고 있다. 정진이는 이 음료들을 섞어 만든 칵테일을 만든다.
# 홀짝 칵테일은 칵테일에 들어가는 음료들의 고유 번호의 곱에 해당하는 맛을 가진다.
#
# 맛이 홀수인 칵테일이 맛이 짝수인 칵테일보다는 무조건 맛있다고 느낀다.
# 또한, 똑같이 홀수이거나 짝수인 맛을 가진 칵테일끼리는 맛이 더 큰 칵테일을 더 맛있다고 느낀다.
#
# 음료 셋의 고유 번호가 주어졌을 때 정진이가 이 음료들을 조합해 만들 수 있는 칵테일 중 가장 맛있다고 느끼는 칵테일의 맛을 알려주자.
# 칵테일을 만들 때는, 반드시 모든 음료를 사용할 필요는 없지만, 적어도 하나의 음료는 사용해야 한다. 하나의 음료만 사용하는 경우 칵테일의 맛은 사용한 음료의 고유 번호와 같다.
# 또한, 주어지는 세 음료는 서로 다른 고유 번호를 가지고 있다.
#
# 입력
# 첫째 줄에는 주어진 세 음료의 고유번호 A, B, C가 주어진다.
#
# 출력
# 첫째 줄에 만들 수 있는 홀짝 칵테일 중 가장 정진이가 맛있다고 느끼는 홀짝 칵테일의 맛을 출력한다.

A, B, C = map(int, input().split())

drinks = [A, B, C, A * B, A * C, B * C, A * B * C]

res = 0
for drink in drinks:
    # res가 짝수, drink 홀수면 교체, 아니면 크면 교체
    if res % 2 == 0 and (drink % 2 == 1 or res < drink):
            res = drink
    # res가 홀수, drink가 홀수이면서 크면 교체
    elif drink % 2 == 1 and res < drink:
            res = drink
print(res)