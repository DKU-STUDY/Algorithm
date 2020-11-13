#include <string>
#include <vector>
#include <iostream>
using namespace std;

int brute_force(vector<int> numbers, int target,int sum,int idx) {
    if (idx == numbers.size()) {
        if (sum == target)
            return 1;
        return 0;
    }

    int plus = brute_force(numbers, target, sum + (1 * numbers[idx]), idx + 1);
    int minus = brute_force(numbers, target, sum + (-1 * numbers[idx]), idx + 1);
    return plus + minus;
}

int solution(vector<int> numbers, int target) {
    int answer = brute_force(numbers, target, 0, 0);
    return answer;
}