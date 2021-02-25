#include <iostream>
#include <stack>
#include <string>

using namespace std;

bool inbalanceStack(string s) {
	stack <char> st;
	for (char c : s) {
		if (c == '(' || c == '{' || c == '[')
			st.push(c);
		else {
			if (st.empty() || (st.top() != c - 1 && st.top() != c - 2))
				return false;
			st.pop();
		}
	}
	return st.empty();
}

int main() {
	int C;
	cin >> C;
	string s;
	while (C--) {
		cin >> s;
		inbalanceStack(s) ? cout << "YES" << "\n" : cout << "NO" << "\n";
	}
}