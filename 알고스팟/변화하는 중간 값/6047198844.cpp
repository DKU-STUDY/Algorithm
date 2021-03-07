#include <iostream>
#include <queue>
using namespace std;

class make_value {
private:
	int a;
	int b;
	long long current_value=1983;
public:
	make_value(int a, int b) {
		this->a = a;
		this->b = b;
	}

	int nextvalue() {
		long long res = current_value;
		current_value = (current_value * a + b) % 20090711;
		return res;
	}
};

//N개의 배열을 생성하면서 중간값을 계속 더한다.
int Changing_value(int a, int b, int N) {
	int res = 0;
	//최소힙
	priority_queue<int,vector<int>,less<int>> left;
	//최대힙
	priority_queue<int, vector<int>,greater<int>> right;
	//생성기
	make_value* mv = new make_value(a, b);
	for (int i = 0; i < N; i++) {
		int left_size = left.size();
		int right_size = right.size();
		int insert_value = mv->nextvalue();
		if (left_size == right_size) {
			if (left.empty() || left.top() <= insert_value) {
				right.push(insert_value);
			}
			else {
				right.push(left.top()); left.pop();
				left.push(insert_value);
			}
			res = (res + right.top()) % 20090711;
		}
		else {
			if (right.top() < insert_value) {
				left.push(right.top()); right.pop();
				right.push(insert_value);
			}
			else {
				left.push(insert_value);
			}
			res = (res + left.top()) % 20090711;
		}
	}
	return res % 20090711;
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		int N, a, b;
		cin >> N >> a >> b;
		cout << Changing_value(a, b, N) << "\n";
	}

}