#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <math.h>

using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
bool check(int real_interval, char sign,int want_interval) {
    if (sign == '=')
        return real_interval == want_interval;
    else if (sign == '>')
        return real_interval > want_interval;
    else
        return real_interval < want_interval;
}

int solution(int n, vector<string> data) {
    string line = "ACFJMNRT";
    int answer = 0;
    do {
        bool flag = true;
        for (string a : data) {
            char front_kakao = a[0];
            char back_kakao = a[2];
            char sign = a[3];
            int want_interval = a[4] - '0';
            int real_interval = abs((int)line.find(front_kakao) - (int)line.find(back_kakao)) - 1;
            if (!check(real_interval, sign, want_interval)) {
                flag = false;
                break;
            }
        }
        if (flag)
            answer++;
    } while (next_permutation(line.begin(), line.end()));
    return answer;
}

int main() {
    cout << solution(2, { "N~F=0", "R~T>2" });
}
///참고 : https://velog.io/@woga1999/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8B%A8%EC%B2%B4%EC%82%AC%EC%A7%84-%EC%B0%8D%EA%B8%B0