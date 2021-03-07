#include <iostream>
#include <algorithm>
using namespace std;

int arr[1001] = {};
int memo[1001] = {};

int bottomup_dp(int n)
{
	int ans = 0;
	//memo[1] = arr[1];
	for (int i = 1; i <= n; i++)
	{
		for (int j = 0; j < i; j++)
			if (arr[i] > arr[j])
				memo[i] = max(memo[i], memo[j] + arr[i]);
	}
	ans = *max_element(&memo[1], &memo[1] + n);
	return ans;
}

int main()
{
	int n;
	cin >> n;

	for (int i = 1; i <= n; i++)
		cin >> arr[i];

	cout << bottomup_dp(n);
}