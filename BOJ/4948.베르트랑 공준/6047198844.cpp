#include <iostream>
#include <algorithm>

using namespace std;

bool check[246913];

void Sieve() {
	for (int i = 2; i <= 123456*2; i++) {
		if (!check[i]) {
			for (int j = i+i; j <= 123456*2; j += i) {
				check[j] = true;
			}
		}
	}
}

int Count(int n) {
	int res = 0;
	for (int i = n+1; i <= 2*n; i++)
		if(!check[i])
			res++;
	return res;
}

int main() {
	Sieve();
	int num;
	while (1) {
		cin >> num;
		if (!num)
			break;
		cout << Count(num) << "\n";
	}
}