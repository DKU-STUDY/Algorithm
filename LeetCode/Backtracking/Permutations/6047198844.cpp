class Solution {
private:
    bool check[21];
    vector<vector<int>> res;
public:
    void makePermutation(vector<int> &temp, vector<int>& nums){
        if(temp.size()==nums.size()){
            res.push_back(temp);
            return;
        }
        
        for(int i = 0; i < nums.size(); i++){
            if(!check[i]){
                check[i] = true;
                temp.push_back(nums[i]);
                makePermutation(temp, nums);
                temp.pop_back();
                check[i] = false;
            }
        }
        return;
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> temp;
        fill_n(check,21,false);
        makePermutation(temp, nums);
        return res;
    }
};