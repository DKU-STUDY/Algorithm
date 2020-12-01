#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<pair<string, int>, string> a, pair<pair<string, int>, string> b) {
    if (a.first.first != b.first.first)
        return a.first.first < b.first.first;
    return a.first.second < b.first.second;
}
vector<string> solution(vector<string> files) {
    vector<string> answer;
    //HEAD , NUMBER , 해당 string으로 저장한다.
    vector <pair<pair<string,int>,string> > res;
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
        res.push_back({ {head,stoi(number)},s });
    }
    stable_sort(res.begin(), res.end(), compare);
    for (auto temp : res)
        answer.push_back(temp.second);
    return answer;
}

int main() {
    solution({ "img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png" });
}