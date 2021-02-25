#include <iostream>
#include <algorithm>
#include <math.h>
#include <string.h>

using namespace std;

int input[1001];
int memo[1001] = {};
//int mod = 1000000;

int bottomup_dp(int n)
{
	memo[0] = 0;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= i; j++)
			if(memo[i] < input[j] + memo[i - j])
				memo[i] = input[j] + memo[i - j];
	return memo[n];
}


int main()
{
	int N;
	cin >> N;

	for (int i = 1; i <= N; i++)
		cin >> input[i];
	cout << bottomup_dp(N);
}