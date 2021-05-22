class Solution {
private:
    vector<int> words[21];
    int check[21];
    vector<string> res;
public:
    void makeSentence(int idx, string s, int maxIdx, vector<string>& wordDict){
        if(idx > maxIdx){
            return;
        }
        if(idx == maxIdx){
            res.push_back(s);
            return;
        }
        
        for(int i : words[idx]){
            //res.push_back(wordDict[i]);
            string temp = s;
            if(temp==""){
                temp = wordDict[i];
            }else{
                temp = temp + " " + wordDict[i];
            }
            makeSentence(idx+wordDict[i].size(),temp,maxIdx, wordDict);
        }
        return;      
    }
    
    bool isEqual(string &s, string word){
        return s==word;
    }
    
    bool isPossible(int idx, string& s, vector<string>& wordDict){
        if(s.size() < idx)
            return false;
        if(check[idx]==1)
            return true;    
        if(check[idx]==-1)
            return false;
        
        for(int i = 0; i < wordDict.size(); i++){
            if(isEqual(wordDict[i],s.substr(idx,wordDict[i].size()))&&
               isPossible(idx+wordDict[i].size(), s, wordDict)){
                words[idx].push_back(i);
            }
        }
        
        check[idx] = words[idx].size() ? 1 : -1;
        return words[idx].size();
    }
    
    
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        fill_n(check,21,0);
        check[s.size()] = 1;
        isPossible(0,s,wordDict);
        makeSentence(0, "", s.size(), wordDict);
        return res;
    }
};