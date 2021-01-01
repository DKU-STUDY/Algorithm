#include <vector>
#include <iostream>
#include <cstring>
using namespace std;

bool check[50001];
void Sieve(){
    int n = 50000;
    memset(check,false,sizeof(bool)*50001);
    check[1] = true;
    for(int i =1;i<=50000;i++){
        if(!check[i])
            for(int j = i+i; j<50000;j+=i)
                check[j]=true;
    }
    return;
}

int brute_force(int idx,int sum, int cnt, vector<int> &nums){
    if(cnt==3){
        if(!check[sum])
            return 1;
        else
            return 0;
    }
    if(idx==nums.size())
        return 0;
    
    int pick = brute_force(idx+1,sum+nums[idx], cnt+1, nums);
    int non_pick = brute_force(idx+1,sum, cnt, nums);
    return pick+non_pick;
}

int solution(vector<int> nums) {
    Sieve();
    return brute_force(0,0,0, nums);
}