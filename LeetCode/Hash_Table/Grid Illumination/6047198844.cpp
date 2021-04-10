class Solution {
private:
    unordered_map <int,int> cols, rows, leftDiag, rightDiag;
    unordered_map <int,unordered_set<int>> lampGrid;
    
    int d[3] = {-1,0,1};
    
public:
    vector<int> gridIllumination(int N, vector<vector<int>>& lamps, vector<vector<int>>& queries) {
        vector<int> ans;

        for(int i = 0; i < lamps.size(); i++){
            int y = lamps[i][0];
            int x = lamps[i][1];
            
            if(lampGrid[y].insert(x).second){
                cols[x]++;
                rows[y]++;
                leftDiag[y-x]++;
                rightDiag[y+x]++;
            }
        }
        
        for(int i = 0; i <queries.size(); i++){
            int y = queries[i][0];
            int x = queries[i][1];
            
            int _ = cols[x]||rows[y]||leftDiag[y-x]||rightDiag[y+x] ? 1 : 0;
            //꺼져있으면 켜져있는 램프가 근처에 있을 확률 0%
            if(_){
                for(int j = 0; j < 9; j++){
                    int dy = y + d[j/3];
                    int dx = x + d[j%3];
                    if(lampGrid[dy].erase(dx)){
                        cols[dx]--;
                        rows[dy]--;
                        leftDiag[dy-dx]--;
                        rightDiag[dy+dx]--;
                    }
                }    
            }
            ans.push_back(_);
        }
        
        return ans;
    }
};