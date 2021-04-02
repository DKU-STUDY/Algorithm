class Solution {
private:
    bool col[9];
    bool CrossLeft[17];
    bool CrossRight[17];
    int max_n;
    
public:
    int makeNQueens(int y){
        if(y==max_n)
            return 1;
        
        int res = 0;
        for(int x = 0; x < max_n; x++){
            if(!col[x]&&!CrossLeft[y+x]&&!CrossRight[max_n-1-y+x]){
                col[x] = CrossLeft[y+x] = CrossRight[max_n-1-y+x] = true;
                res += makeNQueens(y+1);
                col[x] = CrossLeft[y+x] = CrossRight[max_n-1-y+x] = false;
            }
        }
        
        return res;
    }
    
    int totalNQueens(int n) {
        max_n = n;
        return makeNQueens(0);
    }
};