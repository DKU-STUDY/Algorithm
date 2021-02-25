#include <iostream>
#include <queue>
#include <algorithm>

#define LL long long

using namespace std;

int analysisAlien(int K, int N) {
	queue <int> q;
	int qSum = 0; // Q에 들어있는 신호의 합을 모두 저장한다.
	LL resentArrayValue = 1983; // A[i-1]을 저장한다.
	LL signalValue;
	int cnt = 0;
	for (int i = 1; i <= N; i++) {
		//Q에 있는 값과 K가 동일한 경우 -> Q에서 덜어내야함. cnt ++해야함.
		//Q에 있는 값이 큰경우 -> Q에서 덜어내야함.
		while (qSum >= K) {
			if (qSum == K)
				cnt++;
			qSum -= q.front();
			q.pop();
		}
		//Q에 있는 값이 작은 경우
		signalValue = resentArrayValue % 10000 + 1;
		resentArrayValue = (resentArrayValue * 214013 + 2531011) % (LL)pow(2, 32);
		qSum += signalValue;
		q.push(signalValue);
	}
	return cnt;
}


int main() {
	int C;
	cin >> C;
	int K, N;
	while (C--) {
		cin >> K >> N;
		cout << analysisAlien(K, N) << "\n";
	}
}