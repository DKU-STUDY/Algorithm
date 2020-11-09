#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iterator>
#include <iostream>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;

    priority_queue<int, vector<int>, greater<int> > pq;
    for (int temp : scoville)
        pq.push(temp);
    int cnt = 0;
    int check = pq.top();
    while (check < K){
        int first = pq.top(); pq.pop();
        if (pq.empty()) {
            if (first < K)
                return -1;
            else
                return cnt;
        }
        int second = pq.top(); pq.pop();
        int mix = first + (second * 2);
        pq.push(mix);
        cnt++;
        check = pq.top();
    } 
    answer = cnt;
    return answer;
}

int main() {
    cout << solution({ 0,0,0,0,0,0,0,0,0,0,1,1 }, 7);
}