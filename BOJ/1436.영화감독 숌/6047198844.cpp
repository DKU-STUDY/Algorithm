#include <iostream>

using namespace std;

int main() {
	int start = 666;
	int res = 1;
	int temp;
	int N;
	cin >> N;
	while (res != N) {
		start++;
		temp = start;
		int cnt = 0;
		while (temp&&cnt!=3) {
			if (temp % 10 == 6)
				cnt++;
			else
				cnt = 0;
			temp /= 10;
		}
		if (cnt == 3)
			res++;
	}
	cout << start;
}