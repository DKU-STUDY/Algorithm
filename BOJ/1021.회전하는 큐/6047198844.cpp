#include <iostream>
#include <algorithm>
#include <deque>
#include <queue>

using namespace std;

int second(int n, deque<int> &dq) {
	int res = 0;
	while (dq.front()!=n) {
		res++;
		dq.push_back(dq.front());
		dq.pop_front();
	}
	dq.pop_front();
	return res;
}

int third(int n, deque<int> &dq) {
	int res = 0;
	while (dq.front()!=n) {
		res++;
		dq.push_front(dq.back());
		dq.pop_back();
	}
	dq.pop_front();
	return res;
}

int main() {
	queue<int> q;
	deque<int> dq;
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		dq.push_back(i);
	}
	int M;
	cin >> M;
	for (int i = 0; i < M; i++) {
		int _;
		cin >> _;
		q.push(_);
	}
	int res = 0;
	while (!q.empty()) {
		deque<int> sq = dq;
		deque<int> tq = dq;
		int i = second(q.front(), sq);
		int j = third(q.front(), tq);
		if (i > j) {
			dq = tq;
			res += j;
		}
		else {
			dq = sq;
			res += i;
		}
		q.pop();
	}
	cout << res;
}