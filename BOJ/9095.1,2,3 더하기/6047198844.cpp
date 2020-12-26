/*
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수
dp(1) = dp(0);
dp(2) = dp(1) + dp(0);
dp(3) = dp(1) + dp(2) + dp(0);
dp(4) = dp(1) + dp(2) + dp(3);
dp(5) = dp(2) + dp(3) + dp(4);
dp(n) = 시그마 dp(1~n-1)
*/

#include <iostream>

int memo[11];
using namespace std;

int dp(int n)
{
	if (n < 0)
		return 0;
	if (memo[n])
		return memo[n];

	memo[n] = dp(n - 1) + dp(n - 2) + dp(n - 3);
	return memo[n];
}

int main()
{
	int T; int n;
	cin >> T;
	memo[0] = 1;
	for (int i = 0; i < T; i++)
	{
		cin >> n;
		cout << dp(n) << endl;
	}
}

//완전탐색
#include <iostream>
using namespace std;

//base case
//1. 0일떄 1을 반환한다.
//2. 0보다 작을때 0을 반환한다.

//et의 정의.
// n-1 , n-2 , n-3을 더한 값을 반환한다.
int et(int n)
{
	if (n == 0)
		return 1;
	else if (n < 0)
		return 0;
	return et(n - 1) + et(n - 2) + et(n - 3);
}

int main()
{
	int T;
	cin >> T;
	int n;
	for (int i = 0; i < T; i++)
	{
		cin >> n;
		cout << et(n) << endl;
	}
}