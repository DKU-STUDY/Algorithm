#include <iostream>
using namespace std;

int dp[501][501];
int arr[501][501];
int Max = 0,N;
int main(void) {
	cin >> N;
	for(int i=1; i<=N; i++) //[1][1]부터 값을 입력받기 시작합니다. 
		for(int j=1; j<=i; j++) 
			cin >> arr[i][j];
			
 /* 숫자들을 한쪽으로 몰아서 계단 형태로 놓고 보면, 다음 경로로 향할 때
  	가능한 경로는 arr[Y-1][X] 또는 arr[Y-1][X-1] 였습니다. 이 아이디어를 2차원 dp 배열에 적용시켰습니다.*/	
	for(int i=1; i<=N; i++) {
		for(int j=1; j<=i; j++) {
			dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + arr[i][j];
		}
	}
	
	for(int i=1; i<=N; i++) 
		if(dp[N][i] > Max) Max = dp[N][i];
	cout << Max;
	return 0;
}
