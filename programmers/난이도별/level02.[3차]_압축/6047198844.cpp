#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;
//to_string은 int를 string으로.
vector<int> solution(string msg) {
    vector<int> answer;
    map <string, int> mp;
    for (char i = 'A'; i <= 'Z'; i++) {
        string alpha;
        alpha += i;
        mp[alpha] = i - 'A' + 1;
    }

    int cnt = 27;
    //끝에 도달할때까지, 끝에 도달하면 그냥 출력한다.(등록X)
    int msg_size = msg.size();
    string res;
    for (int idx = 0; idx < msg_size; idx++) {
        res += msg[idx];
        if (mp.find(res) != mp.end())
            continue;
        mp[res] = cnt++;
        answer.push_back(mp[res.substr(0, res.size() - 1)]);
        res = "";
        idx--;
    }
    answer.push_back(mp[res]);
    return answer;
}
int main() {
    solution("TOBEORNOTTOBEORTOBEORNOT");
}