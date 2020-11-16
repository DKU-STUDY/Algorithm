#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

int solution(vector<vector<string>> clothes) {
    map <string, int> clothes_cnt;
    int answer = 1;
    for (auto c : clothes)
        clothes_cnt[c[1]]++;
    for (auto m : clothes_cnt)
        answer *= (m.second + 1);
    answer--;
    
    return answer;
}