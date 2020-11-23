#include <string>
#include <vector>

using namespace std;

int zero_one[2] = { 0,0 };
void divide_and_conquer(vector<vector<int>> &arr,int y, int x, int size) {
    if (size == 1) {
        zero_one[arr[y][x]]++;
        return;
    }
    bool check = true;
    for (int i = y; i < y + size; i++) {
        if (!check)
            break;
        for (int j = x; j < x + size; j++) {
            if (arr[y][x] != arr[i][j]) {
                check = false;
                break;
            }
        }
    }
    if (check) {
        zero_one[arr[y][x]]++;
    }
    else {
        divide_and_conquer(arr,y, x, size / 2);
        divide_and_conquer(arr,y + size / 2, x, size / 2);
        divide_and_conquer(arr,y, x + size / 2, size / 2);
        divide_and_conquer(arr,y + size / 2, x + size / 2, size / 2);
    }
    return;
}

vector<int> solution(vector<vector<int>> arr) {
    divide_and_conquer(arr,0, 0, arr[0].size());
    vector<int> answer{ zero_one[0],zero_one[1] };
    return answer;
}