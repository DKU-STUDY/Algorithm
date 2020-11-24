#include <string>
#include <map>
using namespace std;

int solution(string str1, string str2) {
    //소문자 -> 대문자
    int str1_size = str1.size();
    int str2_size = str2.size();

    for (int i = 0; i < str1_size; i++)
        if (str1[i] >= 'a' && str1[i] <= 'z')
            str1[i] = str1[i] - 'a' + 'A';
    for (int i = 0; i < str2_size; i++)
        if (str2[i] >= 'a' && str2[i] <= 'z')
            str2[i] = str2[i] - 'a' + 'A';
    //두글자씩 쪼갠다. 공백이나 숫자. 특수문자가 있는지 체크. 글자쌍 버림
    map <string, int> mp1;
    map <string, int> mp2;

    for (int i = 0; i < str1_size - 1; i++) {
        string s1 = "";
        if ((str1[i] >= 'A' && str1[i] <= 'Z') && (str1[i + 1] >= 'A' && str1[i + 1] <= 'Z')) {
            s1 = s1 + str1[i] + str1[i + 1];
            mp1[s1]++;
        }
    }

    for (int i = 0; i < str2_size - 1; i++) {
        string s2 = "";
        if ((str2[i] >= 'A' && str2[i] <= 'Z') && (str2[i + 1] >= 'A' && str2[i + 1] <= 'Z')) {
            s2 = s2 + str2[i] + str2[i + 1];
            mp2[s2]++;
        }
    }
    int connection = 0;
    for (auto s : mp2) {
        if (mp1[s.first]) {
            if (mp1[s.first] > s.second) {
                connection += s.second;
            }
            else {
                connection += mp1[s.first];
                mp1[s.first] = s.second;
            }
        }
        else {
            mp1[s.first] = s.second;
        }
    }
    int total = 0;
    for (auto s : mp1) {
        total += s.second;
    }
    if(total)
        return (double)connection / (double)total * 65536;
    else
        return 65536;
}

int main() {
    solution("aa1+aa2", "AAAA12");
}