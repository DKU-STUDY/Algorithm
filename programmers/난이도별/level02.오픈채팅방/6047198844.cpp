//map<string,string>을 사용

#include <map>
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <cstring>

using namespace std;

vector<string> solution(vector<string> record) {
    vector<string> answer;
    //Enter이나 Change일때 바꾼다.
    map <string, string> mp;
    vector <vector<string> > vt;
    mp["Enter"] = "들어왔습니다.";
    mp["Leave"] = "나갔습니다.";

    int end_idx = record.size();
    string commend;
    string user_id;
    string user_name;

    for (int i = 0; i < end_idx; i++) {
        char str_buff[50];
        strcpy(str_buff, record.at(i).c_str());
        char* tok = strtok(str_buff, " ");
        commend = string(tok);
        tok = strtok(nullptr, " ");
        user_id = string(tok);
        if (commend == "Enter" || commend == "Leave")
            vt.push_back({ user_id,commend });
        if (commend == "Leave")
            continue;
        tok = strtok(nullptr, " ");
        mp[user_id] = string(tok);
    }
    
    int vt_size = vt.size();
    for (int i = 0; i < vt_size; i++) {
        string temp = mp[vt[i][0]] + "님이 " + mp[vt[i][1]];
        answer.push_back(temp);
    }

    return answer;
}

int main() {
    solution({ "Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan" });
}