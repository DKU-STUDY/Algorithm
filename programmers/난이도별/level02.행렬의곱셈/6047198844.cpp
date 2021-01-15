#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    int arr1_y_size = arr1.size();
    int arr1_x_size = arr1[0].size();
    int arr2_y_size = arr2.size();
    int arr2_x_size = arr2[0].size();
    vector<vector<int>> answer;
    for(int arr1_y = 0;arr1_y<arr1_y_size;arr1_y++){
        vector<int> vt;
        for(int arr2_x=0;arr2_x<arr2_x_size;arr2_x++){
            int element = 0;
            for(int arr1_x_arr2_y = 0; arr1_x_arr2_y < arr1_x_size;arr1_x_arr2_y++){
                element += arr1[arr1_y][arr1_x_arr2_y]*arr2[arr1_x_arr2_y][arr2_x];
            }
            vt.push_back(element);
        }
        answer.push_back(vt);
    }
    return answer;
}