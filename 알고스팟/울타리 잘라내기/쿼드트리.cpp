#include <iostream>
#include <string>

using namespace std;

string quadtree(string s) {
	if (s[0] == 'w' || s[0] == 'b') {
		string ret = "";
		ret += s[0];
		return ret;
	}
	else {
		int idx = 1;
		string res[4];
		for (int i = 0; i < 4; i++) {
			res[i] = quadtree(s.substr(idx));
			idx += res[i].size();
		}
		return s[0] + res[2] + res[3] + res[0] + res[1];
	}
}

int main() {
	int n;
	cin >> n;
	string s;
	while (n--) {
		cin >> s;
		cout << quadtree(s) << "\n";
	}
}