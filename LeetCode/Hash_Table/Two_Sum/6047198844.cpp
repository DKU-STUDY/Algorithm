class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> map;
        for(int i=0; i < nums.size(); i++){
            if(map.find(target - nums[i])==map.end()){
                map[nums[i]] = i;
            }
            else{
                return vector<int>({i,map[target - nums[i]]});
            }
        }
        return vector<int>();
    }
};