#include <iostream>
using namespace std;

long long dp[1001][1001]; //파스칼의 삼각형을 이용했습니다. 따라서 2차원 dp배열을 선언했습니다. 
int N,K;
int main(void) {
	cin >> N >> K;

	for(int i=1; i<=N; i++) { //nC0, nC1은 1이므로 미리 1을 입력합니다. 
		dp[i][0]=1;
		dp[i][i]=1; 
	}
	
	for(int i=2; i<=N; i++) { // 문제에서 10007로 나눈 나머지를 출력하라고 제시했으므로, %10007 연산을 추가해줍니다. 
		for(int j=1; j<=N-1; j++) {
			dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%10007;	
		}
	}
	cout << dp[N][K]; 
	return 0;
}
