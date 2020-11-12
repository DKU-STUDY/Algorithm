#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool true_string(string p) {
    int p_size = p.size(); int cnt = 0;
    for (int i = 0; i < p_size; i++) {
        if (p[i] == '(')
            cnt++;
        else
            cnt--;
        if (cnt < 0)
            return false;
    }
    return true;
}

string kakao(string p) {
    //빈 문자열 반환
    if (p == "")
        return "";
    int cnt = 0;
    int p_size = p.size();

    // ')'경우 +
    // '('경우 - 
    string u = "";
    string v = "";
    int i;
    //"균형잡힌 괄호 문자열로 분리
    for (i=0; i < p_size; i++) {
        if (p[i] == '(')
            cnt++;
        else
            cnt--;
        u += p[i];
        if (cnt == 0)
            break;
    }
    for (int j = i + 1; j < p_size; j++)
        v += p[j];

    //u가 올바른 괄호 문자열인지 판단.
    bool check = true_string(u);
    if (check) {
        return u + kakao(v);
    }
    else {
        string temp = "";
        temp += '(';
        temp += kakao(v);
        temp += ')';
        int u_size = u.size();
        for (int i = 1; i < u_size - 1; i++) {
            if (u[i] == ')')
                temp += '(';
            else
                temp += ')';
        }
        return temp;
    }
}

string solution(string p) {
    string answer = kakao(p);
    return answer;
}

int main() {
    cout << solution(")(");
}