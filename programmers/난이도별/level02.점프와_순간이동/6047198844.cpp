#include <iostream>
#include <algorithm>

using namespace std;

int brute_force(int n) {
    int res = 0;
    while (n) {
        if (n % 2)
            res++;
        n /= 2;
    }
    return res;
}

int solution(int n)
{
    return brute_force(n);
}