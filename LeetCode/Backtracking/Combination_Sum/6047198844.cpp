class Solution {
private:
   vector<vector<int>> res;
    
public:
    void makeCombiSum(vector<int>& candidates,vector<int>&combi, int idx, int sum,int target){
        if(sum>target)
            return;
        if(sum==target){
            res.push_back(combi);
            return;
        }
        
        for(int i=idx; i < candidates.size(); i++){
            combi.push_back(candidates[i]);
            makeCombiSum(candidates,combi, i, sum+candidates[i],target);
            combi.pop_back();
        }
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> combi;
        makeCombiSum(candidates, combi, 0, 0, target);
        return res;
    }
};