#include <iostream>
#define LL long long 
using namespace std;

LL divide_and_conquer(LL A, LL  B, LL C) {
	if (B == 0)
		return 1;
	if (B % 2) {
		return ((A % C) * (divide_and_conquer(A, B - 1, C) % C)) % C;
	}
	else {
		int res = divide_and_conquer(A, B / 2, C);
		return (res % C * res % C) % C;
	}
}

int main() {
	LL A, B, C;
	cin >> A >> B >> C;
	cout << divide_and_conquer(A, B, C);
}