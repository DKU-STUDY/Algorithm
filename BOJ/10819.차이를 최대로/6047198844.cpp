#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <deque>

using namespace std;

int absolute_function(deque <int> &dq, int n, int cnt)
{
	int sum = 0;
	for (int i = 1; i < n; i++)
		sum += abs(dq.at(i - 1) - dq.at(i));

	if (cnt == 1)
		return sum;

	int temp = dq.front();
	dq.pop_front();
	dq.push_back(temp);

	return max(sum, absolute_function(dq, n, cnt - 1));
}

int main()
{
	int N;
	cin >> N;
	deque <int> dq;
	int num;
	for (int i = 0; i < N; i++)
	{
		cin >> num;
		dq.push_back(num);
	}
	cout << absolute_function(dq, N, N);
}