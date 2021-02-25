#include <iostream>
#include <vector>

using namespace std;

int main() {
	int N;
	cin >> N;
	vector <pair<int, int>> hw;
	int weight, height;
	for (int i = 0; i < N; i++) {
		cin >> weight >> height;
		hw.push_back({ weight,height });
	}
	for (int i = 0; i < N; i++) {
		int k = 1;
		for (int j = 0; j < N; j++)
			if (i != j && hw[i].first < hw[j].first && hw[i].second < hw[j].second)
				k++;
		cout << k << " ";
	}
}