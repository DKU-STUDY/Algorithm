#include <vector>
#include <map>
#include <iostream>
using namespace std;

int solution(vector<int> nums)
{
    map <int,int> mp;
    int num_size = nums.size();
    for(int i=0;i<num_size;i++)
        mp[nums[i]]++;
    int mp_size = mp.size();
    int answer = num_size/2 > mp_size ? mp_size : num_size/2;
    return answer;
}