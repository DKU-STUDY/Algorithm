#include <iostream>
#include <algorithm>
#define GOLDMAX 10000

using namespace std;

//true면 prime임.
bool isPrime[10001];

void printPartition(int N) {
	int resPrime = 0;
	//차이를 저장
	int resDif = -1;
	for (int i = 1; i <= N; i++) {
		if (isPrime[i] && isPrime[N - i]) {
			int dif = abs(N - 2 * i);
			if (resDif == -1||resDif > dif) {
				resDif = dif;
				resPrime = i;
			}
		}
	}
	int firstOne = resPrime;
	int secondOne = N - resPrime;
	if (firstOne > secondOne)
		swap(firstOne, secondOne);
	cout << firstOne << " " << secondOne << "\n";
}

void doSieve() {
	fill_n(isPrime, 10000, true);
	isPrime[1] = false;
	for (int i = 2; i <= 10000; i++) {
		if (isPrime[i])
			for (int j = i + i; j < 10000; j += i)
				isPrime[j] = false;
	}
}

int main() {
	
	int T;
	cin >> T;
	doSieve();
	while (T--) {
		int N;
		cin >> N;
		printPartition(N);
	}
}
