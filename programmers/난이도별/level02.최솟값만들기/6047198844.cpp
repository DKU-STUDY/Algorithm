#include <iostream>
#include<vector>
#include <algorithm>
using namespace std;

int solution(vector<int> A, vector<int> B)
{
    int answer = 0;
    sort(A.begin(),A.end());
    sort(B.begin(),B.end());
    int vt_size = A.size();
    for(int i =0; i<vt_size; i++)
        answer += (A[i]*B[vt_size-1-i]);
    return answer;
}