class Solution {
private:
    int memo[1001];
public:
    int makeCombi(vector<int>& nums, int remain){
        if(remain < 0)// if negative numbers are allowed , it should be removed
            return 0;
        if(remain == 0)
            return 1;

        if(memo[remain]!=-1)
            return memo[remain];
        
        int &res = memo[remain];
        res = 0;
        
        for(int i = 0; i < nums.size(); i++){
            res += makeCombi(nums, remain-nums[i]);
        }
        
        return res;
    }
    
    int combinationSum4(vector<int>& nums, int target) {
        memset(memo,-1,sizeof(memo)); // if negative numbers are allowed , it should not be-1 but be changed 
        return makeCombi(nums, target); 
    }
};