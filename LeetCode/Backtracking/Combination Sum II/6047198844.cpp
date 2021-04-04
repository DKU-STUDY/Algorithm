class Solution {
private: 
    vector<vector<int>> res;
public:
    void makeCombi(vector<int>& candidates, vector<int>& temp, int idx, int sum, int target){
        if(sum > target){
            return;
        }
        if(sum == target){
            res.push_back(temp);
        }
        
        for(int i = idx; i < candidates.size()&& candidates[i] <= target; i++){
            if(i==idx||candidates[i-1]!=candidates[i]){
                temp.push_back(candidates[i]);
                makeCombi(candidates, temp, i+1, sum+candidates[i], target);
                temp.pop_back();                
            }
        }
    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        vector<int> temp;
        makeCombi(candidates, temp, 0 , 0, target);
        return res;
    }
};