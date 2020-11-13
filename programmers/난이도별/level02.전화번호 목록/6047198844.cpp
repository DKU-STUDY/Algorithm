#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    sort(phone_book.begin(), phone_book.end());
    map <string, bool> mp;
    for (auto i : phone_book) {
        mp[i] = true;
        int i_size = i.size();
        for (int j = 1; j < i_size; j++) {
            if (mp[i.substr(0, j)]) {
                answer = false;
                break;
            }
            
        }
        if (!answer)
            break;
    }

    return answer;
}

int main() {
    solution({ "97674223", "1195524421","119" });
}