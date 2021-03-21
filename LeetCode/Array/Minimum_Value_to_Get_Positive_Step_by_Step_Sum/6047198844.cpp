class Solution {
public:
    int minStartValue(vector<int>& nums) {
        for(int i = 1; i < nums.size(); i++)
            nums[i] += nums[i-1];
        sort(nums.begin(),nums.end());
        if(nums[0]<0)
            return -nums[0]+1;
        return 1;
    }
};