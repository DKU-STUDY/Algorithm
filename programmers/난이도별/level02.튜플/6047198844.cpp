#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;
bool comp(vector<int> a, vector<int> b) {
    return a.size() < b.size();
}
vector<int> solution(string s) {
    vector<vector<int>> vt;
    int s_start_idx = 0;
    int s_end_idx = s.size() - 1;
    int idx = s_start_idx;
    while(idx < s_end_idx) {
        idx++;
        vector <int> vt_element;
        // }이 나올때까지 원소로 넣는 do while문
        do {
            idx++;
            int e = 0;
            while (s[idx] != ',' && s[idx] != '}')
                e = (e * 10) + (s[idx++] - '0');
            vt_element.push_back(e);
        } while (s[idx] != '}');
        idx++;
        vt.push_back(vt_element);
    }
    sort(vt.begin(), vt.end(), comp);

    vector<int> answer;
    map <int, bool> mp;
    int vt_size = vt.size();
    for (int i = 0; i < vt_size; i++) {
        for (int j = 0; j <= i; j++) {
            if (!mp[vt[i][j]]) {
                mp[vt[i][j]] = true;
                answer.push_back(vt[i][j]);
            }
        }
    }   
    return answer;
}