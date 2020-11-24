#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    //index%인원수 + 1 -> 번호 / (index/인원수) + 1 -> 차례 
    
    //체크해야 할것 
    //1. 뒤와 앞이 맞는지 
    //2. 중복된 글자인지 -> map
    map <string,bool> mp; 
    mp[words[0]] = true;
    int words_size = words.size();
    for(int i=1;i<words_size;i++){
        if((*words[i-1].rbegin()!=*words[i].begin())||mp[words[i]]){
            return {(i%n+1),(i/n+1)};
        }
        mp[words[i]] = true;
    }
    return {0,0};
}