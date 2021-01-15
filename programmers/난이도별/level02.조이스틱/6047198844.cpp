#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string name) {
    int answer = 0;
    int name_size = name.size();
    int left_cursor = name_size - 1;
    int right_cursor = 999999;
    if (name_size >= 2) {
        //커서를 왼쪽으로 이동하는 경우의 수
        for (int i = 1; name[i] == 'A'&&i<name_size; i++) {
            --left_cursor;
        }

        //커서를 왼쪽으로 갔다가 오른쪽으로 다시 이동하는 경우의수
        int a_count = 0; int max_a_count = 0; int start_a = 0; int end_a = 0;
        for (int i = 1; i < name_size; i++) {
            if (name[i] == 'A') {
                start_a = i;
                for (; name[i] == 'A' && i < name_size; i++);
                end_a = i;
                int temp = (start_a - 1) * 2 + (name_size - end_a);
                if (temp < right_cursor || right_cursor == -1)
                    right_cursor = temp;
            }
        }

        ////커서를 오른쪽으로 이동하는 경우의 수
        //for (int i = name_size - 1; name[i] == 'A'&&i>0; i--) {
        //    --right_cursor;
        //}


    }
    int cursor_cnt = left_cursor > right_cursor ? right_cursor : left_cursor;

    int name_cnt = 0;
    int up_cursor;
    int down_cursor;
    for (auto i : name) {
        up_cursor = 'Z' - i + 1;
        down_cursor = i - 'A';
        if (up_cursor > down_cursor)
            name_cnt += down_cursor;
        else
            name_cnt += up_cursor;
    }

    answer = name_cnt + cursor_cnt;
    return answer;
}
