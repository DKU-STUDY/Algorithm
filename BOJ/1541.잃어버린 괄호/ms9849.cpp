#include <iostream>
using namespace std;

int result=0,tmp;
string s;
int Flag = 0;

int main(void) {
	
	cin >> s;
	int len = s.length();
	
	for(int i=0; i<=s.length(); i++) {
		if(s[i] == '+' || s[i] == '-' || i== len) {
			if(Flag == 0) result += tmp;
			else result -= tmp;
			tmp = 0;
			
			if(s[i] == '-') Flag = 1;
		}
		else {
			tmp *= 10;
			tmp += s[i] -'0';
		}
	}	
	cout << result;
	return 0;
}
