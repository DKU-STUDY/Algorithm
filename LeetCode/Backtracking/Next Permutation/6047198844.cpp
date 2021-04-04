class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int cur = nums.size();        
        while(cur--){
            if(cur==0){
                sort(nums.begin(),nums.end());
                return;
            }
                
            
            int &beforeValue = nums[cur-1];
            int &currentValue = nums[cur];
            
            if(beforeValue < currentValue){
                sort(nums.begin()+cur,nums.end());
                int changedIdx = upper_bound(nums.begin()+cur,nums.end(),nums[cur-1]) - nums.begin();
                swap(nums[cur-1],nums[changedIdx]);
                return;
            }
        }
        
    }
};