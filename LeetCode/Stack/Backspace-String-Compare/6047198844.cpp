class Solution {
public:
    string makeString(string s){
        string res;
        for(char c : s){
            if(c=='#'){
                if(!res.empty()) res.pop_back();    
            }
            else
                res.push_back(c);
        }
        return res;
    }
    bool backspaceCompare(string S, string T) {
        S = makeString(S) ;
        T = makeString(T) ;
        return S==T;        
    }
};