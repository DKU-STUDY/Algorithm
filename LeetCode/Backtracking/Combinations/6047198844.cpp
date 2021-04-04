class Solution {
//1~N 범위에서의 모든 조합
    private:
    int max_n;
    vector<vector<int>> res;
    public:
    void makeCombi(int idx, vector<int> &combinations, int remain){
        if(remain==0){
            res.push_back(combinations);
            return;
        }
        for(int i = idx+1; i <= max_n; i++){
            combinations.push_back(i);
            makeCombi(i,combinations,remain-1);
            combinations.pop_back();           
        }
        return;
    }
    vector<vector<int>> combine(int n, int k) {
        max_n = n;
        vector<int> combinations;
        makeCombi(0,combinations,k);
        return res;
    }
};