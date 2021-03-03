#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

bool cmp(const string a, const string b) {
	if (a.size() != b.size())
		return a.size() < b.size();
	return a < b;
}

int main() {
	int N;
	cin >> N;
	vector<string> arr;
	string s;
	for (int i = 0; i < N; i++) {
		cin >> s;
		arr.push_back(s);
	}
	sort(arr.begin(), arr.end(), cmp);
	arr.erase(unique(arr.begin(), arr.end()), arr.end());
	for (int i = 0; i < arr.size(); i++)
		cout << arr[i] << "\n";
}