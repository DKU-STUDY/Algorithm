#include <string>
#include <vector>

using namespace std;

int brute_force(int n){
    int res = 0;
    int sum;
    for(int i=1;i<=n;i++){
        sum = 0;
        for(int j=i;j<=n;j++){
            sum+=j;
            if(sum>=n){
                if(sum==n)
                    res++;
                break;
            }
        }
    }
    return res;
}

int solution(int n) {
    int answer = 0;
    answer = brute_force(n);
    return answer;
}