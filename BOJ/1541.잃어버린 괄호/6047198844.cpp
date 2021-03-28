#include <iostream>
#include <vector>

using namespace std;

int main() {
	vector<int> arr;
	int N;
	cin >> N;
	char op;
	arr.push_back(N);
	while (cin >> op >> N) {
		if (op == '-')
			arr.push_back(N);
		else 
			arr[arr.size() - 1] = arr.back() + N;
	}
	int res = arr[0];
	for (int i = 1; i < arr.size(); i++)
		res -= arr[i];
	cout << res;
}
```