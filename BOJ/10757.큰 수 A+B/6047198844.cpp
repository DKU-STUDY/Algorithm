#include <iostream>
#include <string>

using namespace std;

int main() {
	string a;
	string b;
	cin >> a >> b;
	while (a.length() != b.length()) {
		if (a.length() > b.length())
			b = '0' + b;
		else if (a.length() < b.length())
			a = '0' + a;
	}
	string res = "";
	int temp = 0;
	int aIdx = a.length() - 1, bIdx = b.length() - 1;
	for (; aIdx >= 0 && bIdx >= 0; aIdx--, bIdx--) {
		int digit = temp + a[aIdx] + b[bIdx] - 2*'0';
		temp = digit / 10;
		digit %= 10;
		res = char(digit + '0') + res;
	}
	if(temp)
		res = char(temp + '0') + res;
	cout << res;
}