#include <string>
#include <vector>
#include <cstring>
#include <iostream>
using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    int alphabet[26];
    memset(alphabet, 0, sizeof(int) * 26);
    int cnt = 1;
    for (auto a : skill)
        alphabet[a - 'A'] = cnt++;
    
    for (string s : skill_trees) {
        int check = true;
        int current_skill = 1;
        for (int idx = 0; idx < s.size(); idx++) {
            if (!alphabet[s[idx] - 'A'])
                continue;
            if (alphabet[s[idx] - 'A'] == current_skill)
                current_skill++;
            else {
                check = false;
                break;
            }
        }
        if (check)
            answer++;
    }
    return answer;
}