class Solution {
private:
    string num[8] = {"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    vector<string>res;
    
public:
    void dfs(string temp, string digits){
        if(digits=="")
                return res.push_back(temp);
        int numIdx = digits[0]-'0';
        for(char c : num[numIdx-2])
            dfs(temp+c,digits.substr(1));
    }
    
    vector<string> letterCombinations(string digits) {
        if(digits.size())
            dfs("", digits);
        return res;
    }
};