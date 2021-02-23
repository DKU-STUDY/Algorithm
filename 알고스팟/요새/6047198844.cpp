#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;


struct fortress_tree
{
	vector<int> my_node = { 0,0,0 };
	vector<fortress_tree*> child;
	bool operator < (const fortress_tree &fortress_tree) {
		return fortress_tree.my_node[2] < this->my_node[2];
	}
};

int sqr(int x) {
	return x * x;
}


int height(fortress_tree& side_wall) {
	int res = 0;
	int size = side_wall.child.size();
	for (int i = 0; i < size; i++) {
		res = max(res, 1 + height(*side_wall.child[i]));
	}
	return res;
}

bool make_tree(fortress_tree &side_wall, fortress_tree &circle) {
	//만약에 이 서클이 side_wall 내부에 존재하고 child의 내부에 존재하지 않을때 child에 넣는다.
	//만약 이 서클이 side_wall 외부에 존재하는 경우 parent의 child를 이 서클로 바꾸고 이 서클의 child를 side_wall로 한다.
	int side_wall_x = side_wall.my_node[0];
	int side_wall_y = side_wall.my_node[1];
	int side_wall_r = side_wall.my_node[2];
	int circle_x = circle.my_node[0];
	int circle_y = circle.my_node[1];
	int circle_r = circle.my_node[2];

	//side_wall은 기존의 원이고 circle은 삽입하고자하는 원임
	int d = sqr(side_wall_y - circle_y) + sqr(side_wall_x - circle_x);
	int r = sqr(side_wall_r - circle_r);

	//원의 내부에 존재한다.
	if (r > d) {
		int child_size = side_wall.child.size();
		for (int i = 0; i < child_size; i++) {
			if (make_tree(*side_wall.child[i], circle)) {
				return true;
			}
		}
		side_wall.child.push_back(&circle);
		return true;
	}
	return false;
}

//루트 노드를 거치는 노드와 노드사이 가장 긴 길이를 구한다.
int nodeToNode(fortress_tree& side_wall) {
	vector<int> child_node = { 0,0 };
	int res = 0;
	int child_size = side_wall.child.size();
	for (int i = 0; i < child_size; i++) {
		child_node.push_back(1 + height(*side_wall.child[i]));
	}
	sort(child_node.begin(), child_node.end(), greater<int>());
	res = child_node[0] + child_node[1];
	for (int i = 0; i < child_size; i++) {
		res = max(res, nodeToNode(*side_wall.child[i]));
	}
	return res;
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		int N;
		cin >> N;
		vector<fortress_tree> circle(N);
		for (int i = 0; i < N; i++)
			cin >> circle[i].my_node[0] >> circle[i].my_node[1] >> circle[i].my_node[2];

		fortress_tree side_wall;
		side_wall = circle[0];
		sort(circle.begin(), circle.end());
		for (int i = 1; i < circle.size(); i++) {
			make_tree(side_wall, circle[i]);
		}

		//vector<int> res{ 0,0 };
		//int root_child_size = side_wall.child.size();
		//for (int i = 0; i < root_child_size; i++) {
		//	res.push_back(dfs(*side_wall.child[i]));
		//}
		//sort(res.begin(), res.end(),greater<int>());
		//cout << res[0] + res[1] << "\n";
		int res = nodeToNode(side_wall);
		cout << res << "\n";
	}
}