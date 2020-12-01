#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<pair<string, int>, pair<int, string> > a, pair<pair<string, int>, pair<int, string> > b) {
    if (a.first.first != b.first.first)
        return a.first.first < b.first.first;
    else if (a.first.second != b.first.second)
        return a.first.second < b.first.second;
    else
        return a.second.first < b.second.first;
}
vector<string> solution(vector<string> files) {
    vector<string> answer;
    //HEAD , NUMBER , 들어온순서, 해당 string으로 저장한다.
    vector <pair<pair<string,int>, pair<int,string> > > res;
    //대문자는 소문자로 변경한다.
    int cnt = 0;
    for (string s : files) {
        int idx = 0;
        string head;
        for (; ('0' > s[idx] || s[idx] > '9'); idx++) {
            head += 'A' <= s[idx] && s[idx] <= 'Z' ? s[idx] - 'A' + 'a' : s[idx];
        }
        string number;
        for (; '0' <= s[idx] && s[idx] <= '9';idx++) {
            number += s[idx];
        }
        res.push_back({ {head,stoi(number)},{cnt++,s} });
    }
    sort(res.begin(), res.end(), compare);
    for (auto temp : res)
        answer.push_back(temp.second.second);
    return answer;
}

int main() {
    solution({"F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"});
}