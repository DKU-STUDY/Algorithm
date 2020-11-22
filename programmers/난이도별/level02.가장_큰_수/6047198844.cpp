#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;

bool compare(string a, string b) {
    return (a + b) > (b + a);
}

string solution(vector<int> numbers) {
    vector<string> s_numbers;
    string answer = "";
    for (auto i : numbers)
        s_numbers.push_back(to_string(i));
    sort(s_numbers.begin(), s_numbers.end(), compare);
    for (auto i : s_numbers)
        answer += i;
    return answer = answer[0]!='0' ? answer : "0";
}

int main() {
    solution({ 6,10,2 });
}