#include <string>
#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;

long long caluate(vector <string> token) {
    string pmm = "*+-";
    long long max_num = -1;
    do {
        vector<string> res = token;
        for (char sign : pmm) {
            if (sign == '-') {
                for (int i = 1; i < res.size(); i += 2) {
                    if (res[i] == "-") {
                        res.insert(res.begin() + i - 1, to_string(stoll(res[i - 1]) - stoll(res[i + 1])));
                        res.erase(res.begin() + i, res.begin() + i + 3);
                        i += -2;
                    }
                }
            }
            else if (sign == '+'){
                for (int i = 1; i < res.size(); i += 2) {
                    if (res[i] == "+") {
                        res.insert(res.begin() + i - 1, to_string(stoll(res[i - 1]) + stoll(res[i + 1])));
                        res.erase(res.begin() + i, res.begin() + i + 3);
                        i += -2;
                    }
                }
            }
            else {
                for (int i = 1; i < res.size(); i += 2) {
                    if (res[i] == "*") {
                        res.insert(res.begin() + i - 1, to_string(stoll(res[i - 1]) * stoll(res[i + 1])));
                        res.erase(res.begin() + i, res.begin() + i + 3);
                        i += -2;
                    }
                }
            }
        }
        max_num = max_num < abs(stoll(res[0])) ? abs(stoll(res[0])) : max_num;
    } while (next_permutation(pmm.begin(), pmm.end()));
    return max_num;
}


vector<string> tokenize(string expression) {
    vector<string> token;
    int expression_size = expression.size();
    for (int i = 0; i < expression_size; i++) {
        string num;
        while ('0' <= expression[i] && expression[i] <= '9') {
            num += expression[i];
            i++;
        }
        token.push_back(num);
        string sign;
        sign += expression[i];
        if (i != expression_size)
            token.push_back(sign);
        //to_string은 정수형으로 바꾼뒤 string으로 바꾼다.
    }
    return token;
}

long long solution(string expression) {
    vector <string> res = tokenize(expression);
    return caluate(res);
}

int main() {
    solution("100-200*300-500+20");
}