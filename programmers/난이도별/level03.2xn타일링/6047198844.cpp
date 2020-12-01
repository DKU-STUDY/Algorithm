#include <string>
#include <vector>

using namespace std;

int memo[60001] = {1};
int dp(int n) {
    return
        n < 0 ? 0 :
        memo[n] ? memo[n] :
        memo[n] = (dp(n - 2) + dp(n - 1))%1000000007;
}

int solution(int n) {
    return dp(n);
}