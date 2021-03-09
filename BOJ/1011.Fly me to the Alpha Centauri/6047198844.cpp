#include <iostream>

using namespace std;
#define fastio cin.sync_with_stdio(false); cin.tie(nullptr)
/*
=> 이전 단계에서 k광년 이동시 k-1 , k , k + 1 , 즉 처음엔 -1 , 0 , 1 
=> 도착 지점 바로 직전의 거리는 1광년

거리 이동거리  공간 이동장치 이동 횟수
1    1         1
2    11        2
3    111       3
4    121       3
5    1211      4
6    1221      4
7    12211     5
8    12221     5
9    12321     5
10   123211    6
11   123221    6
12   123321    6
13   1233211   7
14   1233221   7
15   1233321   7
16   1234321   7
17   12343211  8
18   12343221  8
...

이동횟수    개수    누적합
1           1        1
2           1        2
3           2        4
4           2        6
5           3        9
6           3        12
7           4        16
8           4        20
9           5        25
10          5        30

개수의 쌍을 한묶음으로 보았을때 n(n+1)은 두번째 값의 뒤경계값이 됩니다.
이전쌍의 두번째 값의 뒤에 있는 누적합 + 1이 됩니다. = n^2-n+1
따라서 n에 따른 경계는 다음과 같습니다. n^2-n+1 <= <= n^2+n
2를 대입해보면 2개를 가지고 있는 이동횟수 3과 4의 경계를 구할수있습니다.
3 <= <= 6

3를 대입해보면 3개를 가지고 있는 이동횟수 5과 6의 경계를 구할수있습니다.
7 <= <= 12

즉 만든 경계식에 n을 1부터 증가시키면서 주어진 거리에 포함되는지 여부를 판단하고
해당 경계에서 또 세분화된 경계를 구할수있습니다.
n^2-n+1 <= <= n^2 은 첫번째 값의 경계일것이고,
n^2+1 <= <= n^2+n은 두번째 값의 경계일것입니다.

큰 범위를 구하고 세부 범위에 속하는지 판단하면 됩니다.
제곱에 있어서 범위를 조심해야겠습니다.
*/

int range(int distance) {
	//distance의 범위는 1~2^31-1 입니다.
	//distance가 2^31-1때 범위구하는 연산에서 overflow를 주의해야할것입니다.
	long long N = 0;
	long long begin;
	long long end;
	long long powN;
	while (1) {
		N++;
		long long powN = N * N;
		begin = powN - N + 1;
		end = powN + N;
		if (begin <= distance && distance <= end) {
			begin = powN + 1;
			//뒤에 위치하는 경우
			if (begin <= distance && distance <= end)
				return N << 1;
			//앞에 위치하는 경우
			else
				return (N << 1) - 1;
		}
	}
}

int main() {
	fastio;
	int _;
	cin >> _;
	int x, y;
	while (_--) {
		cin >> x >> y;
		cout << range(y - x) << "\n";
	}
}