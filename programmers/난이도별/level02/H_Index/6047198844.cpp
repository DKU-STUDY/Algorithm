#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

int solution(vector<int> citations) {
    int length = citations.size();
    sort(citations.begin(), citations.end());
    int res = 0;
    for (int i = 0; i <= length; i++){
        if (i <= (length)-(lower_bound(citations.begin(), citations.end(), i) - citations.begin()))
            res = i;
        else
            break;
    }
    return res;
}