#include <iostream>
#include <vector>

using namespace std;

int main() {
	int N;
	vector<int> arr(10);
	while (~scanf("%1d", &N))
		++arr[N];
	for (int i = 9; i >= 0; i--)
		while(arr[i]--)
			cout << i;
}