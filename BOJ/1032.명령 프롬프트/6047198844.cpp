#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int N;
	cin >> N;
	vector <string> vt;
	string temp;
	while (N--) {
		cin >> temp;
		vt.push_back(temp);
	}
	int size = vt[0].size();
	string res;
	//O(n^2) n¿Ã 50
	bool flag = true;
	for (int idx = 0; idx < size; idx++) {
		flag = true;
		for (string s : vt) {
			if (s[idx] != vt[0][idx]) {
				flag = false;
				res.push_back('?');
				break;
			}
		}
		if (flag)
			res.push_back(vt[0][idx]);
	}
	cout << res;
}
