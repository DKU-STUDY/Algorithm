#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int INF = 987654321; 
int length; 
int arr[100], partSum[100], partSquareSum[100];
int cache[100][10];


void preCalculate(void){
    sort(arr, arr + length);
    partSum[0] = arr[0];
    partSquareSum[0] = arr[0] * arr[0];
    for (int i = 1; i < length; i++){
        partSum[i] = partSum[i - 1] + arr[i];
        partSquareSum[i] = partSquareSum[i - 1] + arr[i] * arr[i];
    }
}

int minDiffrence(int low, int high){
    int sum = partSum[high] - (low == 0 ? 0 : partSum[low - 1]);
    int squareSum = partSquareSum[high] - (low == 0 ? 0 : partSquareSum[low - 1]);
    int mean = (int)(0.5 + (double)sum / (high - low + 1));
    int result = squareSum - (2 * mean * sum) + (mean * mean * (high - low + 1));
    return result;
}

int quantize(int from, int parts) {
    if (from == length)
        return 0;
    if (parts == 0)
        return INF;
    int& result = cache[from][parts];
    if (result != -1)
        return result;
    result = INF;
    for (int partSize = 1; from + partSize <= length; partSize++)
        result = min(result, minDiffrence(from, from + partSize - 1) + quantize(from + partSize, parts - 1));
    return result;
}
int main(void){
    int s;
    cin >> s;
    for (int i = 0; i < s; i++){
        int useNum;
        cin >> length >> useNum;
        for (int i = 0; i < length; i++)
            cin >> arr[i];
        preCalculate();
        memset(cache, -1, sizeof(cache));
        cout << quantize(0, useNum) << endl << endl;
    }
    return 0;
}