#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
    char* s_p = new char[s.size()];
    vector <int> vt;
    strcpy(s_p, s.c_str());
    char* ptr = strtok(s_p, " "); 
    while (ptr != NULL)
    {
        vt.push_back(stoi(ptr));
        ptr = strtok(NULL, " ");
    }
    string answer = " ";
    int min = *min_element(vt.begin(),vt.end());
    int max = *max_element(vt.begin(), vt.end());
    return to_string(min)+answer+to_string(max);
}