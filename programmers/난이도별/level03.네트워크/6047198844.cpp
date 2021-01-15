#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool computer_node[201];
void dfs(int num,vector<vector<int>>& computers) {
    if (computer_node[num]) {
        return;
    }
    computer_node[num] = true;
    int computers_size = computers.size();
    for (int i = 0; i < computers_size; i++) {
        if (computers[num][i])
            dfs(i, computers);
    }
    return;
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    for (int i = 0; i < n; i++) {
        if (!computer_node[i]) {
            dfs(i, computers);
            answer++;
        }
    }
    return answer;
}

int main() {
    cout << solution(3, { {1, 1, 0 }, { 1, 1, 1 }, { 0, 1, 1 }});
}