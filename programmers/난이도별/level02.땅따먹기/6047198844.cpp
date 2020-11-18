#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// memo[N][0] // 0번째 열을 택했을때의 최대값.
// memo[N][1] // 1번째 열을 택했을때의 최대값.
// memo[N][2] // 2번째 열을 택했을때의 최대값.
// memo[N][3] // 3번째 열을 택했을때의 최대값.

int memo[100000][4];
//row, column -> 현재 row / 이전에 선택한 column
//dp(N,0) = dp(N-1,1)+land[N][1] , dp(N-1,2)+land[N][2],dp(N-1,3)+land[N][3]
int dp(int row, int column, vector<vector<int> >& land) {
    if (row == -1)
        return 0;
    if (memo[row][column])
        return memo[row][column];

    int res = 0;
    for (int i = 0; i < 4; i++) {
        if (i != column) {
            int temp = dp(row - 1, i, land) + land[row][i];
            memo[row][column] = memo[row][column] > temp ? memo[row][column] : temp;
        }
    }
    return memo[row][column];
}


int solution(vector<vector<int> > land)
{
    int answer = 0;

    int row = land.size() - 1;
    return dp(row, 5, land);
}