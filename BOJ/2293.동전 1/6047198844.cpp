/*
d[0] = 1;

	1		2		3		4		5		6		7		8		9		10
1	1		1		1		1		1		1		1		1		1		1  
	d[0]	d[1]	d[2]	d[3]	d[4]	d[5]	d[6]	d[7]	d[8]	d[9]

2	1		2		2		3		3		4		4		5		5		6
			d[0]	d[1]	d[2]	d[3]	d[4]	d[5]	d[6]	d[7]	d[8]

5	1		2		2		3		4		5		6		7		8		10
									d[0]	d[1]	d[2]	d[3]	d[4]	d[5]

3 10
1
2
5

*/

#include <iostream>
#include <algorithm>

using namespace std;

int value[10001] = { 1 };
int coin[100];

int dp(int n, int k) {
	/*
	for (int coin_idx = 0; coin_idx < n; coin_idx++)
		for (int value_idx = 1; value_idx <= k; value_idx++) {
			if(value_idx - coin[coin_idx]>=0)
				value[value_idx] += value[value_idx - coin[coin_idx]];
		}
	*/
	for (int coin_idx = 0; coin_idx < n; coin_idx++)
		for (int a = coin[coin_idx]; a <= k; a++)
			value[a] += value[a - coin[coin_idx]];
	return value[k];
}

int main() {
	int n; int k;
	cin >> n >> k;
	for (int i = 0; i < n; i++)
		cin >> coin[i];
	cout << dp(n, k);
}