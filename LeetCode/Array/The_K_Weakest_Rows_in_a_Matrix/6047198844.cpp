class Solution {
public:
    static bool compare(pair<int,int> &a, pair<int,int> &b){
        if(a.first != b.first)
            return a.first < b.first;
        return a.second < b.second;
    }
    
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        int n = mat[0].size();
        vector< pair<int,int> > tmp;
        
        for(int i = 0 ; i < mat.size(); i++){
            int soldierN = n - (lower_bound(mat[i].rbegin(),mat[i].rend(),1) - mat[i].rbegin());
            tmp.push_back({soldierN,i});                    
        }
            
        sort(tmp.begin(),tmp.end(),compare);
        
        vector<int> res;
        for(int i = 0; i < k ; i++)
            res.push_back(tmp[i].second);
        return res;
    }
};
