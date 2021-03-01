#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
	int N;
	cin >> N;
	vector<int> arr(N);
	map<int, int> fr_mp;
	double average = 0;
	int sum = 0;
	int center = 0;
	//최빈값의 빈도횟수
	int frequency = 0;
	//최빈값
	int frequency_value = 0;
	int range = 0;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];

		sum += arr[i];
		fr_mp[arr[i]]++;
		if (frequency < fr_mp[arr[i]])
			frequency = fr_mp[arr[i]];
	}
	sort(arr.begin(), arr.end());
	//average = sum<0 ? ((sum * 10) / N - 5) / 10 : ((sum * 10) / N + 5) / 10;
	average = sum / double(N);
	center = arr[N / 2];
	vector<int> fr_vt;
	for (map<int, int>::iterator it=fr_mp.begin(); it != fr_mp.end(); it++) {
		if (it->second == frequency)
			fr_vt.push_back(it->first);
	}
	sort(fr_vt.begin(), fr_vt.end());
	if (fr_vt.size() == 1)
		frequency_value = fr_vt[0];
	else
		frequency_value = fr_vt[1];
	range = arr[N - 1] - arr[0];
	printf("%.0f\n", average);
	cout << center << "\n" << frequency_value << "\n" << range;
}