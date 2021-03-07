#include <iostream>
#include <queue>
#define fastio cin.sync_with_stdio(false); cin.tie(nullptr)

using namespace std;

int main() {
	fastio;

	priority_queue<int, vector<int>, less<int>> left;
	priority_queue<int, vector<int>, greater<int>> right;
	/*
		시간제한은 0.1초이다.
		N이 100,000 이기 때문에. 일반 배열을 사용할수없다. 
		일반 배열을 사용하면 탐색에 O(1) , 중앙에 삽입에 O(N)의 시간이 걸린다. 
		삽입을 N번하므로 . O(N^2) 시간이 걸린다. 1초를 넘긴다.

		우선순위큐를 사용해서 푼다.
		우선순위큐는 새 원소를 추가하는 연산 / 최대,최소원소를 꺼내는 연산을 O(lgN) 시간에 수행한다.
		따라서 100,000 * 16 == 1,600,000 이므로 1천만이 안된다. 가능하다.

		두개의 우선순위큐를 사용한다.
		현재 가지고 있는 배열을 오름차순으로 정렬한뒤 반으로 나눈다.
		두가지 규칙을 세운다.
		1. 왼쪽 배열은 오른쪽 배열보다 개수가 1개 많거나 같다. -> 먼저 만족
		2. 왼쪽 배열의 top값은 오른쪽 배열의 top값보다 작다.  -> 이후 만족
	*/


	int N;
	cin >> N;
	int num;
	while (N--) {
		cin >> num;
		//같은 경우 항상 left에 넣어야 1번 규칙이 만족된다.
		if (left.size() == right.size())
			left.push(num);
		//왼쪽이 하나더 많은 경우 항상 right에 넣어야 1번 규칙이 만족된다.
		else
			right.push(num);
		//왼쪽이 비는 경우는 존재하지 않는다. 오른쪽이 비는 경우는 존재할수있다. 왼쪽에 하나 있고 오른쪽에 없는 경우이다.
		//여기서는 오른쪽이 비지 않았을때 두개의 값을 비교한다.
		if (!right.empty() && left.top() > right.top()) {
			int leftMax = left.top();
			int rightMin = right.top();
			left.pop(); left.push(rightMin);
			right.pop(); right.push(leftMax);
		}
		cout << left.top() << "\n";
	}
}