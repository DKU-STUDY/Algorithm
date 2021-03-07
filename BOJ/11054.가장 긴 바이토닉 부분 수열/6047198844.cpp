#include <iostream>
#include <algorithm>
using namespace std;

int arr[1001] = {};
int memo_a[1001] = {};
int memo_d[1001] = {};

int bottomup_dp(int n)
{
	int ans = 0;

	fill(&memo_a[1], &memo_a[n+1], 1);
	fill(&memo_d[1], &memo_d[n+1], 1);

	for (int i = 2; i <= n; i++)
		for (int j = 1; j < i; j++)
			if (arr[i] > arr[j])
				memo_a[i] = max(memo_a[i], memo_a[j] + 1);

	for (int i = n - 1; i > 1; i--)
		for (int j = n; j > i; j--)
			if (arr[i] > arr[j])
				memo_d[i] = max(memo_d[i], memo_d[j] + 1);

	for (int i = 1; i <= n; i++)
		ans = max(ans, memo_a[i] + memo_d[i] - 1);

	return ans;
}


int main()
{
	int n;
	cin >> n;

	for (int i = 1; i <= n; i++)
		cin >> arr[i];

	cout << bottomup_dp(n) << "\n";
}
