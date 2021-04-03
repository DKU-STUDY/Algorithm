class Solution {
private:
    vector<vector<int>> res;
public:
    void makeCombi(int k, int n,vector<int> &temp, int idx, int sum){
        if(sum > n||temp.size()>k){
            return;
        }
        
        if(sum == n){
            if(temp.size()==k)
                res.push_back(temp);
            return;
        }
        
        for(int i = idx; i <= 9; i++){
            temp.push_back(i);
            makeCombi(k, n,temp, i+1, sum+i);
            temp.pop_back();
        }
        
        return;
    }
    
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> temp;
        makeCombi(k,n,temp,1,0);
        return res;
    }
};