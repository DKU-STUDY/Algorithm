#include <iostream>

using namespace std;

int brute_force(int N){
    for(int i = 1; i <= 1000000; i++){
        int res = i;
        int temp = i;
        while(temp){
            res += temp % 10;
            temp /= 10;
        }
        if(res==N)
            return i;
    }
    return 0;
}

int main()
{
    int N;
    cin >> N;
    cout << brute_force(N);
    return 0;
}
