#include <string>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

string detobi(int n) {
    string s = "";
    while (n) {
        s = to_string(n % 2) + s;
        n = n / 2;
    }
    return s;
}

int bitode(string n) {
    int res = 0;
    int end_index = n.size() - 1;
    for (int i = 0, j = 1; i <= end_index; i++,j*=2) {
        res += (n[end_index - i] - '0') * j;
    }
    return res;
}


int solution(int n) {
    int answer = 0;
    string res = detobi(n);
    if (find(res.begin(), res.end(), '0') == res.end())
        res.insert(1, "0");
    else
        next_permutation(res.begin(), res.end());
    if (res[0] == '0') {
        next_permutation(res.begin(), res.end());
        res.insert(1, "0");
    }
        
    answer = bitode(res);
    return answer;
}

int main() {
    solution(6);
}