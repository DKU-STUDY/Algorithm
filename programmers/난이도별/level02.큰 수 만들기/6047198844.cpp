//#include <string>
//#include <vector>
//#include <cstring>
//#include <iostream>
//using namespace std;
//
//int res_max = 0;
//
//void brute_force(string number, string res, int idx, int cnt, int k) {
//    if (cnt == k) {
//        int temp = stoi(res);
//        if (temp > res_max)
//            res_max = temp;
//        return;
//    }
//    if (number.size() <= idx)
//        return;
//
//    선택했을때
//    brute_force(number, res + number[idx], idx + 1, cnt + 1, k);
//    선택하지않았을때
//    brute_force(number, res, idx + 1, cnt, k);
//    return;
//}
//
//string solution(string number, int k) {
//    string answer = "";
//    brute_force(number, "", 0, 0, number.size() - k);
//    answer = to_string(res_max);
//    return answer;
//}

#include <string>
#include <vector>
using namespace std;

string solution(string number, int k) {
    string answer = "";
    int start_idx = 0;
    int end_idx = k;
    int number_size = number.size();
    for (int end_idx = k; end_idx < number_size; end_idx++) {
        char temp = '0';
        int temp_start_idx;
        for (int i = start_idx; i <= end_idx; i++) {
            if (number[i] > temp) {
                temp = number[i];
                temp_start_idx = i;
            }
        }
        start_idx = temp_start_idx + 1;
        answer += temp;
    }

    return answer;
}