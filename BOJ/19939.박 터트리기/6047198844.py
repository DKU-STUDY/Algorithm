"""
1. N개의 공을 K개의 바구니에 빠짐없이 나누어 담는다.
2. 각 바구니에는 1개 이상의 공이 들어 있어야 한다.
3. 각 바구니에 담긴 공의 개수는 모두 달라야 한다.
4. 가장 많이 담긴 바구니와 가장 적게 담긴 바구니의 공의 개수 차이가 최소가 되어야 한다.

N개의 공을 K개의 바구니에 나눠 담을 때, 나눠 담을 수 있는지 여부를 결정하고, 담을 수 있는 경우에는 가장 많이 담긴 바구니와 가장 적게 담긴 바구니의 공의 개수 차이를 계산해서 출력하시오.

최소값을 i라고 하자.
이상적인 상황은 i, i+1, i+2, i+3, i+(K-1) 일 것이다. (마지막값이 K-1이상의 값을 가지면된다.)
i는 최소 배분가능한 개수이다.
i는 N / K가 초기값이 될것이다. 1까지 감소한다. 감소 조건은 끝까지 분배가 안될경우 줄여나간다.
--> 로직이 틀렸다

일단 1부터 K개를 배분한다. -> 공의 개수가 모두 다르게 표현된다.
남은 공들을 K개 부터 역순으로 배분한다 -> 1부터 배분할 경우 공의 개수가 같아 질수있다.
=> 배분이 똑같이 이루어진다면, 차이는 K-1일것이다.  (나머지가 K의 배수인 경우, 0포함)
=> 배분이 균일하게 이루어지지 않는다면, 차이는 K일것이다.
"""

N, K = map(int, input().split())
min_portion = (1 + K) * K // 2
remain = N - min_portion
if remain >= 0:
    if remain % K == 0:
        print(K - 1)
    else:
        print(K)
else:
    print(-1)
