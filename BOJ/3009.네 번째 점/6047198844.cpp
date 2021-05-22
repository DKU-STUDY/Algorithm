#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int x[3];  int y[3];
	int N = 3;
	while (N--) {
		cin >> x[N] >> y[N];
	}
	sort(x, x + 3);
	sort(y, y + 3);
	x[0] == x[1] ? cout << x[2] : cout << x[0];
	cout << " ";
	y[0] == y[1] ? cout << y[2] : cout << y[0];
}