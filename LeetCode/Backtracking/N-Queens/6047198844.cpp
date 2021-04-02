class Solution {
private:
    vector<vector<string>> res;
    vector<string> chessBoard;
    bool col[9];
    bool crossLeft[17];
    bool crossRight[17];
public:
    
    
    void makeNQueens(int n, int y){
        if(n==y){
            res.push_back(chessBoard);
            return;
        }
        string s(n,'.');
        for(int x = 0; x<n; x++){
            if(!col[x]&&!crossLeft[y+x]&&!crossRight[n-1-y+x]){
                col[x] = true;
                crossLeft[y+x] = true;
                crossRight[n-1-y+x] = true;
                s[x] = 'Q';
                chessBoard.push_back(s);
                makeNQueens(n, y+1);
                chessBoard.pop_back();
                s[x] = '.';
                crossRight[n-1-y+x] = false;
                crossLeft[y+x] = false;
                col[x] = false;
            }
        }
        return;
    }
    
    vector<vector<string>> solveNQueens(int n) {
        makeNQueens(n,0);
        return res;
    }
};