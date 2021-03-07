#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector <int> slice(vector <int> &vt, int a, int b) {
	vector <int> svt(vt.begin() + a, vt.begin() + b);
	return svt;
}

//후위 순회한다.
void postOrder(vector <int> preOrder) {
	if (!preOrder.size())
		return;
	int root = preOrder[0];
	int idx = upper_bound(preOrder.begin(), preOrder.end(), root) - preOrder.begin();

	postOrder(slice(preOrder, 1, idx));
	postOrder(slice(preOrder, idx, preOrder.size()));
	cout << root << "\n";
}

int main() {
	vector <int> preOrder;
	string num;
	while (getline(cin, num))
		preOrder.push_back(stoi(num));
	postOrder(preOrder);
}