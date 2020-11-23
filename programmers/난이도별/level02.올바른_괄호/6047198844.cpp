#include<string>
#include <iostream>

using namespace std;

bool solution(string s)
{
    int cnt = 0;
    for(auto idx : s){
        if(idx=='(')
            cnt++;
        else
            cnt--;
        if(cnt<0)
            return false;
    }
    return cnt==0;
}