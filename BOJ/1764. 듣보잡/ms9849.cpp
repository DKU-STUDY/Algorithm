#include <iostream>
#include <algorithm>
using namespace std;

string s[1000000];
string ans[500000];
int N,M,cnt=0;

int main(void) {
	cin >> N >> M;
	for(int i=0; i<N; i++) 
		cin >> s[i];
		
	for(int j=N; j<N+M; j++)
		cin >> s[j];
		
	sort(s,s+N+M);
	
	for(int i=1; i<N+M; i++) {
		if(s[i]==s[i-1]) {
			ans[cnt] = s[i];
			cnt++;
		}	
	}
	
	cout << cnt << "\n";
	for(int i=0; i<cnt; i++) cout << ans[i] << "\n";
	
	return 0;
}
