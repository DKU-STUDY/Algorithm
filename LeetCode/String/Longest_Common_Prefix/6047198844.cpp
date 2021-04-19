class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int minSize = 0;
        for(int i = 0; i < strs.size(); i++)
            if(!minSize||minSize < strs[i].size()) minSize = strs[i].size();
        
        
        for(int j = 0; j < minSize; j++){
            for(int i = 1; i < strs.size(); i++){
                if(strs[0][j] != strs[i][j])
                    return strs[0].substr(0,j);
            }    
        }
    
        return strs.size() ? strs[0] : "";
    }
};