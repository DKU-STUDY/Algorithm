#include <vector>
#include <iostream>
using namespace std;

bool primenum(int n) {
	if (n <2) return false;
	for (int i = 2; i < n / 2; i++) {
		if (n % i == 0) return false;
	}
	return true;
}
int solution(vector<int> nums) {
	int answer = 0;
	int numSize = nums.size();
	int sum = 0;
	for (int i = 0; i < numSize; i++) {
		for (int j = i + 1; j < numSize; j++) {
			for (int k = j + 1; k < numSize; k++) {
				sum = nums[i] + nums[j] + nums[k];
				if (primenum(sum)) answer++;
			}
		}
	}

	return answer;
}
