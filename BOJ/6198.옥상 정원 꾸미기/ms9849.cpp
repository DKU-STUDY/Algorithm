#include <iostream>
#include <stack>
#include <vector>
using namespace std;

//monotone stack을 이용하여 풀이 

int N,num,ans=0;
stack<int> s;
vector<int> v;

int main(void) {
	cin >> N;
	
	for(int i=0; i<N; i++) {
		cin >> num;
		v.push_back(num);
	}
	
	for(int i=0; i< N; i++) { // monotone stack을 만드는 과정. 내림차순으로 유지된다. 
		while(!s.empty() && s.top() <= v[i]) s.pop(); 
		s.push(v[i]);
		ans += s.size() - 1; /* monotone stack으로 만들면 현재 자신을 볼 수 있는 건물의 수만큼 stack에 쌓여있다.
		 이 때 자기 자신도 stack에 존재하므로 -1을 수행*/
	}
	cout << ans;
	return 0;
}
