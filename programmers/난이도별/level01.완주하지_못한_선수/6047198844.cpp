#include <string>
#include <vector>
#include <map>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    map <string, int> mp;
    for (auto completion_person : completion)
        mp[completion_person]++;
    for (auto participant_person : participant)
        mp[participant_person]--;
    for (auto answer_check : mp)
        if (answer_check.second)
            return answer_check.first;
}