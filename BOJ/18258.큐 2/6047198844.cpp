#include <iostream>

using namespace std;

int q[2000001];
int head = 0;
int tail = 0;

//empty : 큐가 비어있으면 1, 아니면 0을 출력한다.
bool isEmpty() {
	return head == tail;
}

//push X : 정수 X를 큐에 넣는 연산이다.
void push(int X) {
	q[tail++] = X;
	tail = tail % 2000000;
}

//pop : 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.만약 큐에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
void pop() {
	if (isEmpty())
		cout << "-1";
	else {
		cout << q[head++];
		head = head % 2000000;
	}
	cout << "\n";
}

//size : 큐에 들어있는 정수의 개수를 출력한다.
void size() {
	cout << abs(tail - head) << "\n";
}

//front : 큐의 가장 앞에 있는 정수를 출력한다.만약 큐에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
void front() {
	if (isEmpty())
		cout << -1;
	else
		cout << q[head];
	cout << "\n";
	return;
}
//back : 큐의 가장 뒤에 있는 정수를 출력한다.만약 큐에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
void back() {
	if (isEmpty())
		cout << -1;
	else {
		if (tail == 0)
			cout << q[2000000];
		else
			cout << q[tail - 1];
	}
	cout << "\n";
	return;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;
	while (N--) {
		string s;
		cin >> s;
		if (s == "push") {
			int X;
			cin >> X;
			push(X);
		}
		else if (s == "pop")
			pop();
		else if (s == "size")
			size();
		else if (s == "empty") {
			if (isEmpty())
				cout << "1";
			else
				cout << "0";
			cout << "\n";
		}
		else if (s == "front")
			front();
		else
			back();
	}
}