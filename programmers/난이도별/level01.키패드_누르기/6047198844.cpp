#include <string>
#include <vector>
#include <math.h>

using namespace std;


string answer = "";

void left(int &current_left,string &answer,int click){
    current_left = click;
    answer += 'L';
}
void right(int &current_right,string &answer,int click){
    current_right = click;
    answer += 'R';
}

string solution(vector<int> numbers, string hand) {
    int current_left = 10;
    int current_right = 12;
    for (auto click : numbers) {
        if (!click)
            click = 11;
        if (click % 3 == 1) {
            left(current_left,answer,click);
        }
        else if (click % 3 == 0) {
            right(current_right,answer,click);
        }
        else {
            int left_distance = abs(current_left - click) / 3 + abs(current_left - click) % 3;
            int right_distance = abs(current_right - click) / 3 + abs(current_right - click) % 3;
            if (left_distance < right_distance)
                left(current_left,answer,click);
            else if (left_distance > right_distance)
                right(current_right,answer,click);
            else{
                if (hand == "left")
                    left(current_left,answer,click);
                else
                    right(current_right,answer,click);
            }
        }
    }
    return answer;
}

int main() {
    solution({ 1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5 }, "right");
}