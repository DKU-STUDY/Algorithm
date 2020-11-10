#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iterator>
#include <iostream>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;

    priority_queue<int, vector<int>, greater<int> > pq(scoville.begin(), scoville.end());
    int check = pq.top();
    while (check < K) {
        if (pq.size() == 1)
            return -1;
        int first = pq.top(); pq.pop();
        int second = pq.top(); pq.pop();
        int mix = first + (second * 2);
        pq.push(mix);
        answer++;
        check = pq.top();
    }
    return answer;
}
