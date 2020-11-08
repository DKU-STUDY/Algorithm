#include <string>
#include <vector>
#include <iostream>

using namespace std;
// 100*100 = 10000 < 1억 따라서 부르트포스

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    //결과값을 저장
    vector<int> answer;
    //idx는 움직이면서 size에 도달하게 되면 멈춘다.
    int idx = 0;
    while (idx < progresses.size()) {
        for (int i = 0; i < progresses.size(); i++)
            progresses[i] += speeds[i];
        int cnt = 0;
        //idx가 넘어갈경우를 고려해야함
        while (idx < progresses.size()&&progresses[idx] >= 100) {
            cout << cnt << " "<<idx << " "<<progresses[idx] << "\n";
            cnt++, idx++;    
        }
        if (cnt)
            answer.push_back(cnt);
    }
    return answer;
}