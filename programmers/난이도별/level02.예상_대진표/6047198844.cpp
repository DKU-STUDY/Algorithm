#include <iostream>

using namespace std;

int solution(int n, int a, int b)
{
    int cnt;
    for(cnt = 0;a!=b;cnt++){
        a = a/2 + a%2;
        b = b/2 + b%2;
    }
    return cnt;
}