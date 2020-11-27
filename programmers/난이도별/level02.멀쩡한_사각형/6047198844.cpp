#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

long long solution(int w, int h) {
    long long answer = 0;
    long long temp = 0;
    // y = (h/w) * x
    double d_w = (double)w;
    double l_h = (double)h;

    for (int x = 1; x <= w; x++) {
        temp = ceil((l_h / d_w) * x);
        answer += (h - temp);
    }
    answer *= 2;
    return answer;
}

int main() {
    cout << solution(8, 12);
}