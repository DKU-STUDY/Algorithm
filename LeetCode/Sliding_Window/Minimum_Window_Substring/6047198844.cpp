class Solution {
public:
    string minWindow(string s, string t) {
        map <char,int> reqAlphabet;
        for(char c : t)
            reqAlphabet[c]++;
        int startPointer = 0;
        int endPointer = 0;
        int n = s.size();
        string resS = ""; 
        while(startPointer!=n){
            //현재 찾았는가
            bool flag = true;
            for(auto it:reqAlphabet)
                if(it.second>0){
                    flag = false;
                    break;
                }
            //t가 s에 포함되는 경우
            if(flag){
                int findSize = endPointer - startPointer;
                if(resS.size()==0||resS.size()>findSize)
                    resS = string(s.begin()+startPointer,s.begin()+endPointer);
                if(reqAlphabet.find(s[startPointer])!=reqAlphabet.end())
                    reqAlphabet[s[startPointer]]++;
                startPointer++;
            }
            //t가 s에 포함되지 않는 경우
            else{
                //더 이상 확장이 안되는 경우
                if(endPointer==n)
                    return resS;
                if(reqAlphabet.find(s[endPointer])!=reqAlphabet.end())
                    reqAlphabet[s[endPointer]]--;
                endPointer++;
            }
            
        }
        return resS;
    }
};