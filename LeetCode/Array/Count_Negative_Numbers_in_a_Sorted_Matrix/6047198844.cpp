class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int res = 0;
        for(auto g : grid){
            res += upper_bound(g.rbegin(),g.rend(),-1) - g.rbegin();
        }
        return res;
    }
};