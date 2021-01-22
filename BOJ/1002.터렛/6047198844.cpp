#include <iostream>
#include <math.h>

using namespace std;

int main() {
	int T;
	int x1, y1, r1, x2, y2, r2;
	long long d;
	cin >> T;
	while (T--) {
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		d = pow(x1 - x2, 2) + pow(y1 - y2, 2);
		if (pow(r1 - r2,2) < d && d < pow(r1 + r2,2)) {
			cout << "2\n";
			continue;
		}
		else if (x1 == x2 && y1 == y2 && r1 == r2) {
			cout << "-1\n";
			continue;
		}
		else if (pow(r1 - r2,2) == d || d == pow(r1 + r2,2)) {
			cout << "1\n";
			continue;
		}
		else {
			cout << "0\n";
		}
	}
}