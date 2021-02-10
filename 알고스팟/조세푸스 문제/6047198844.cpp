#include <list>
#include <iostream>

using namespace std;

void josephus(int N, int K) {
	list<int> survivors;
	for (int i = 1; i <= N; i++)
		survivors.push_back(i);

	list<int>::iterator kill = survivors.begin();

	while (N > 2) {
		kill = survivors.erase(kill);
		if (kill == survivors.end())
			kill = survivors.begin();
		N--;
		for (int cnt = 1; cnt < K; cnt++) {
			kill++;
			if (kill == survivors.end())
				kill = survivors.begin();
		}
	}
	cout << survivors.front() << " " << survivors.back() << "\n";
}

int main() {
	int C;
	cin >> C;
	int N, K;
	while (C--) {
		cin >> N >> K;
		josephus(N, K);
	}
}
