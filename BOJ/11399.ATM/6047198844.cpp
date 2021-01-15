#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int N, input;
	int sum = 0;
	
	cin >> N;
	vector <int> vt;
	for (int i = 0; i < N; i++)
	{
		cin >> input;
		vt.push_back(input);
	}
	sort(vt.begin(),vt.end());
	for (int i = 0; i < N; i++)
		sum += (N - i) * vt[i];
	cout << sum;
}