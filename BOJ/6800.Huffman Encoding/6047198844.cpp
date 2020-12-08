#include <iostream>
#include <map>

using namespace std;

int main() {
	int N;
	cin >> N;
	map <string, string> mp;
	string word;
	string code;

	for (int i = 0; i < N; i++) {
		cin >> word >> code;
		mp[code] = word;
	}

	string encoded_code;
	string w;
	string res;
	cin >> encoded_code;
	for (char c : encoded_code) {
		w += c;
		if (mp.find(w) != mp.end()) {
			res += mp[w];
			w = "";
		}
	}
	cout << res;
}