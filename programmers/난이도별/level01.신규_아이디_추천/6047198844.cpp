#include <string>
#include <vector>

using namespace std;

//새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때,
//입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것


/*
규칙
 - 아이디의 길이는 3자 이상 15자 이하여야 합니다
 - 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
 - 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
 -  7단계의 순차적인 처리 과정
*/
string level7(string& new_id) {
    string level7Id = new_id;
    while (level7Id.size() <= 2)
        level7Id += new_id.back();
    return level7Id;
}

string level6(string& new_id) {
    if (new_id.size() >= 16) {
        new_id = new_id.substr(0, 15);
        if (new_id.back() == '.')
            new_id.pop_back();
    }
    return level7(new_id);
}

string level5(string& new_id) {
    if (new_id.empty())
        new_id += 'a';
    return level6(new_id);
}

string level4(string& new_id) {
    if (new_id[0] == '.')
        new_id = new_id.substr(1);
    if (new_id.back() == '.')
        new_id.pop_back();
    return level5(new_id);
}

string level3(string& new_id) {
    string level3Id = "";
    bool flag = false;
    for (int i = 0; i < new_id.size(); i++) {
        if (!flag|| new_id[i] != '.') {
            if (new_id[i] == '.')
                flag = true;
            else
                flag = false;
            level3Id += new_id[i];
        }
    }
    return level4(level3Id);
}

string level2(string& new_id) {
    string level2Id = "";
    for (char c : new_id) {
        if (c == '-' || c == '_' || c == '.' ||
            ('a' <= c && c <= 'z') ||
            ('0' <= c && c <= '9'))
            level2Id += c;
    }
    return level3(level2Id);
}

string level1(string& new_id) {
    for (int idx = 0; idx < new_id.size(); idx++) {
        if ('A' <= new_id[idx] && new_id[idx] <= 'Z')
            new_id[idx] += 32;
    }
    return level2(new_id);
}

string level_start(string& new_id) {
    return level1(new_id);
}

string solution(string new_id) {
    string answer = level_start(new_id);
    return answer;
}

int main() {
    solution("...!@BaT#*..y.abcdefghijklm");
}