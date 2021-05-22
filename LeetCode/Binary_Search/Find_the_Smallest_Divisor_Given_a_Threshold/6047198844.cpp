class Solution {
public:
    int smallestDivisor(vector<int>& nums, int threshold) {
        int start = 1;
        int end = 1e6;
        
        while(start < end){
            int mid = (start + end) / 2;
            int sum = 0;
            for(int i = 0; i < nums.size(); i++){
                // sum += nums[i] % mid ? nums[i]/mid + 1: nums[i]/mid;
                sum += (nums[i] + mid - 1)/ mid; 
            }
            
            if(sum > threshold){
                start = mid + 1;
            }else{
                end = mid;
            }
        }
        return start;
    }
};