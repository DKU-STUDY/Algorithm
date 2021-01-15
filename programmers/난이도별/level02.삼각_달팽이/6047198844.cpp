#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int n) {
    int arr[1000][1000];
    int current_y = -1; int current_x = 0;
    int num = 0;

    int add_y[3] = { +1,0,-1 };
    int add_x[3] = { 0,+1,-1 };

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n-i; j++) {
            num++;
            current_y += add_y[i % 3];
            current_x += add_x[i % 3];
            arr[current_y][current_x] = num;
        }
    }

    vector<int> answer;
    for (int y = 0; y < n; y++)for (int x = 0; x <= y; x++) {
        if (arr[y][x])
            answer.push_back(arr[y][x]);
    }
            
    return answer;
}

int main() {
    solution(4);
}