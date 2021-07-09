#include <iostream>
using namespace std;

int N;
int dp[1000001];
int Num_dp[1000001];

int main(void) {
	cin >> N;
	Num_dp[1];
	for(int i=2; i<=N; i++) { //bottom up 방식을 이용했습니다. 비슷한 문제인 1463번 문제에서 숫자들을 저장하는 Num_dp를 선언하여 확장한 개념입니다.
		dp[i] = dp[i-1] +1;
		Num_dp[i] = i-1;
		if(i%2==0 && dp[i] > dp[i/2] + 1) {
			dp[i] = dp[i/2] + 1;
			Num_dp[i] = i/2;
		}
		if(i%3==0 && dp[i] > dp[i/3] + 1) {
			dp[i] = dp[i/3] + 1;
			Num_dp[i] = i/3;	
		}
	}
	cout << dp[N] << "\n";
	while(N!=0) {
		cout << N << " ";
		N = Num_dp[N];
	}
}
