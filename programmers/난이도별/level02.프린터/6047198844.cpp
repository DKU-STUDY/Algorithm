#include <string>
#include <vector>
#include <deque>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    deque <pair<int, int> > dq;

    //dq에는 위치(i)와 중요도 (priorities)가 저장된다.
    int priorities_size = priorities.size();
    for (int i = 0; i < priorities_size; i++)
        dq.push_back({ i,priorities[i] });
    int dq_size = dq.size(); int print_location = -1;
    //원하는 위치가 print되게 되면 반복문을 빠져나갑니다.
    while (location != print_location) {
        bool check = true;
        //q의 맨앞에 있는 중요도가 뒤에 있는 중요도보다 작다면 출력이 불가능합니다. check를 false로 합니다.
        for (int i = 1; i < dq_size; i++) {
            if (dq[0].second < dq[i].second) {
                check = false;
                break;
            }
        }
        //check가 true인 경우 프린트합니다. 프린트했으니 순서(answer)도 증가합니다.
        if (check) {
            print_location = dq.front().first;
            answer++;
        }
        //check가 false인 경우 프린트되지않았습니다. dq의 맨뒤에 놓습니다. (push_back합니다.)       
        else
            dq.push_back(dq.front());
        dq.pop_front();
    }

    return answer;
}