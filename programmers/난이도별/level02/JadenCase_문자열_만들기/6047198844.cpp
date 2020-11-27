#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    int s_size = s.size();
    if (s[0] >= 'a' && s[0] <= 'z')
        s[0] = 'A' + s[0] - 'a';
    for (int idx = 1; idx < s_size; idx++) {       
        if (s[idx-1] == ' ') {
            if (s[idx] >= 'a' && s[idx] <= 'z')
                s[idx] = 'A' + s[idx] - 'a';
        }
        else if(s[idx] >= 'A' && s[idx] <= 'Z'){
            s[idx] = 'a' + s[idx] - 'A';
        }      
    }
    return s;
}