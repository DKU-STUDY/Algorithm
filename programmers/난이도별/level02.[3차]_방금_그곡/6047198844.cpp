#include <string>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


/*
    musicinfors[i] = 음악의 재생시간,음악의 종료시간,실제음
    끝까지 하나의 연속이라도 없으면 탈출
    #가 있는지 판단
*/
bool compare(pair<pair<int, int>, string>& a, pair<pair<int, int>, string>& b) {
    //running_time / 들어온 순서 / 반환값
    if (a.first.first != b.first.first)
        return a.first.first > b.first.first;
    return a.first.second < b.first.second;
}

string solution(string m, vector<string> musicinfos) {
    vector <pair<pair<int, int>, string> > res_string;
    int musicinfos_size = musicinfos.size();
    //모든 음악정보를 탐색한다.
    for (int i = 0; i < musicinfos_size; i++) {
        vector <string> token_string;
        char temp[5000];
        strcpy(temp, musicinfos[i].c_str());
        char* tok;
        tok = strtok(temp, ",");
        while (tok) {
            string temp;
            temp += tok;
            token_string.push_back(temp);
            tok = strtok(NULL, ",");
        }
        int hour = stoi(token_string[1].substr(0, 2)) - stoi(token_string[0].substr(0, 2));
        int minute = stoi(token_string[1].substr(3, 2)) - stoi(token_string[0].substr(3, 2));
        int running_time = hour * 60 + minute;
        //C#는 / D# / F# / G# / A#를 치환한다.
        string current_music;
        string memory_music;
        int memory_size = m.size();
        for (int i = 0; i < memory_size - 1; i++) {
            if (m[i + 1] == '#')
                memory_music += (m[i++] + 30);
            else
                memory_music += m[i];
        }
        if (m[memory_size - 1] != '#')
            memory_music += m[memory_size - 1];


        int current_size = token_string[3].size();
        for (int i = 0; i < current_size - 1; i++) {
            if (token_string[3][i + 1] == '#')
                current_music += (token_string[3][i++] + 30);
            else
                current_music += token_string[3][i];
        }
        if (token_string[3][current_size - 1] != '#')
            current_music += token_string[3][current_size - 1];

        bool check = false;
        int current_music_idx = 0;
        int memory_music_idx = 0;

        int current_music_size = current_music.size();
        int memory_music_size = memory_music.size();
        int temp_current_music_idx = 0;

        for (; current_music_idx < running_time; current_music_idx++) {
            if (current_music[current_music_idx % current_music_size] == memory_music[memory_music_idx]) {
                memory_music_idx++;
                if (memory_music_idx == memory_music_size) {
                    check = true;
                    break;
                }
            }
            else {
                memory_music_idx = 0;
                current_music_idx = temp_current_music_idx++;
            }
        }
        if (check)
            res_string.push_back({ { running_time,i }, token_string[2] });
    }
    if (!res_string.size())
        return "(None)";
    sort(res_string.begin(), res_string.end(), compare);
    return res_string[0].second;
}

int main() {
    cout << solution("ABC", { "12:00,12:14,cdcdf,cdcdcdf", "12:00,12:15,CORRECT,CDEFGAB","12:00,12:14,HELLO,CDEFGAB","12:00,12:14,HELLO,CDEFGAB" });
}