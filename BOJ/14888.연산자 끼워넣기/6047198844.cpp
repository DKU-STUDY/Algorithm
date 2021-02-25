#include <iostream>
#include <vector>

using namespace std;

int res_min = 1000000000;
int res_max = -1000000000;
int N;

//res (¿¬»ê) number[idx]À» °è»êÇØ¼­ res¿¡ ³Ö´Â´Ù. 
void brute_force(vector<int> const number, vector<int>& oper, int idx, int res) {
	//¼±ÅÃÀ» ÇÏÁö ¾Ê´Â´Ù.
	if (idx == N) {
		if (res > res_max)
			res_max = res;
		if (res < res_min)
			res_min = res;
		return;
	}

	//¼±ÅÃÀ» ÇÏ´Â °æ¿ì
	//µ¡»ù . »¬¼À. °ö¼À. ³ª´°¼À
	for (int i = 0; i < 4; i++) {
		if (oper[i] > 0) {
			--oper[i];
			switch (i) {
				case 0: brute_force(number, oper, idx + 1, res + number[idx]);
					break;
				case 1: brute_force(number, oper, idx + 1, res - number[idx]);
					break;
				case 2: brute_force(number, oper, idx + 1, res * number[idx]);
					break;
				case 3: brute_force(number, oper, idx + 1, res / number[idx]);
					break;
			}
			++oper[i];
		}
	}
	return;
}

int main() {
	cin >> N;
	vector<int> number(N);
	for (int i = 0; i < N; i++)
		cin >> number[i];
	vector <int> oper(4);
	for (int i = 0; i < 4; i++)
		cin >> oper[i];
	brute_force(number, oper, 1, number[0]);
	cout << res_max << "\n";
	cout << res_min << "\n";
}
