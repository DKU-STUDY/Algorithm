#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <iostream>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    queue <int> wait_q;
    int truck_weights_size = truck_weights.size();
    for (int i = 0; i < truck_weights_size; i++) {
        wait_q.push(truck_weights[i]);
    }
    deque <pair<int, int> > on_deq; int on_weight = 0;
    int sec = 0;
    do {
        sec++;
        if (on_deq.empty() || wait_q.size()&&(weight >= on_weight + wait_q.front())) {
            on_deq.push_back({ wait_q.front(),0 }); wait_q.pop();
            on_weight += on_deq.back().first;
        }
        for (int i = 0; i < on_deq.size(); i++)
            on_deq[i].second++;
        if (on_deq.front().second == bridge_length) {
            on_weight -= on_deq.front().first;
            on_deq.pop_front();
        }
    } while (on_deq.size() || wait_q.size());
    answer = ++sec;
    return answer;
}

int main() {
    cout << solution(2, 10, {7,4,5,6});
}