#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector <int> slice(const vector <int>& order, int begin, int end) {
	return vector<int>(order.begin() + begin, order.begin() + end);
}

//후위 순회를 출력하는 함수.
//preorder은 root를 알려준다.
//inorder은 preorder에서 얻은 root를 기준으로 좌측 서브 트리와 우측 서브 트리를 구할수있게 한다
void printPost(const vector <int>& preorder, const vector <int>& inorder) {
	if (preorder.empty())
		return;
	int treeSize = preorder.size();
	int root = preorder[0];
	const int L = find(inorder.begin(), inorder.end(), root) - inorder.begin();
	//좌측 서브 트리 후위 방문
	printPost(slice(preorder, 1, L + 1), slice(inorder, 0, L));
	//우측 서브 트리 후위 방문
	printPost(slice(preorder, L + 1, treeSize), slice(inorder, L + 1, treeSize));
	//이제 루트 출력
	cout << root << " ";
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		int N;
		int num;
		cin >> N;
		vector <int> preorder;
		for (int i = 0; i < N; i++) {
			cin >> num;
			preorder.push_back(num);
		}
		vector <int> inorder;
		for (int i = 0; i < N; i++) {
			cin >> num;
			inorder.push_back(num);
		}
		printPost(preorder, inorder);
		cout << "\n";
	}
}