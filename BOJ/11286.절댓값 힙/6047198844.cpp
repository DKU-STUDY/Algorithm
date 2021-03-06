/*
문제
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

배열에 정수 x (x ≠ 0)를 넣는다.
배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 
절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

입력
첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 
만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 
입력되는 정수는 -2^31보다 크고, 2^31보다 작다.

출력
입력에서 0이 주어진 회수만큼 답을 출력한다. 
만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
*/
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
//최대힙 (음수)
class maxHeap {
private:
	vector<int> maxHeap;
public:
	//힙 추가후 조정 연산
	//부모보다 크면 올라간다.
	void push_adj(int idx) {
		//부모가 없는 경우
		if (idx == 0)
			return;
		//부모가 있는 경우
		int parentIdx = (idx - 1) / 2;
		if (maxHeap[idx] > maxHeap[parentIdx]) {
			swap(maxHeap[idx], maxHeap[parentIdx]);
			push_adj(parentIdx);
		}
		return;
	}
	//힙 추가 연산 , N을 추가한다.
	void push(int N) {
		maxHeap.push_back(N);
		push_adj(maxHeap.size() - 1);
		return;
	}

	//힙 삭제후 조정 연산
	void del_adj(int idx) {
		int leftIdx = idx * 2 + 1;
		int rightIdx = idx * 2 + 2;
		int maxIdx = maxHeap.size() - 1;
		//자식이 없는 경우
		//자식 둘(왼쪽 자식)이 없는 경우
		if (leftIdx > maxIdx)
			return;
		
		//자식 둘중 큰 자식을 고른다.
		int maxChildIdx;
		//자식 하나(오른쪽 자식)이 없는 경우
		if (leftIdx == maxIdx)
			maxChildIdx = leftIdx;
		//자식이 둘있는 경우
		else
			maxChildIdx = maxHeap[leftIdx] >= maxHeap[rightIdx] ? leftIdx : rightIdx;
		
		if (maxHeap[maxChildIdx] > maxHeap[idx]) {
			swap(maxHeap[maxChildIdx], maxHeap[idx]);
			del_adj(maxChildIdx);
		}
		return;
	}
	//힙 삭제 연산 -> 삭제값 반환
	int del() {
		int res = maxHeap[0];
		maxHeap[0] = maxHeap.back();
		maxHeap.pop_back();
		del_adj(0);
		return res;
	}
	//empty 체크도함.
	int getMaxValue() {
		return maxHeap.empty() ? 0 : maxHeap[0];
	}
};


//최소힙 (양수)
class minHeap {
private:
	vector<int> minHeap;
public:
	//힙 추가후 조정 연산
	//부모보다 작으면 올라간다.
	void push_adj(int idx) {
		//부모가 없는 경우
		if (idx == 0)
			return;
		//부모가 있는 경우
		int parentIdx = (idx - 1) / 2;
		if (minHeap[idx] < minHeap[parentIdx]) {
			swap(minHeap[idx], minHeap[parentIdx]);
			push_adj(parentIdx);
		}
		return;
	}
	//힙 추가 연산 , N을 추가한다.
	void push(int N) {
		minHeap.push_back(N);
		push_adj(minHeap.size() - 1);
		return;
	}

	//힙 삭제후 조정 연산
	void del_adj(int idx) {
		int leftIdx = idx * 2 + 1;
		int rightIdx = idx * 2 + 2;
		int maxIdx = minHeap.size() - 1;
		//자식이 없는 경우
		//자식 둘(왼쪽 자식)이 없는 경우
		if (leftIdx > maxIdx)
			return;

		//자식 둘중 큰 자식을 고른다.
		int minChildIdx;
		//자식 하나(오른쪽 자식)이 없는 경우
		if (leftIdx == maxIdx)
			minChildIdx = leftIdx;
		//자식이 둘있는 경우
		else
			minChildIdx = minHeap[leftIdx] <= minHeap[rightIdx] ? leftIdx : rightIdx;

		if (minHeap[minChildIdx] < minHeap[idx]) {
			swap(minHeap[minChildIdx], minHeap[idx]);
			del_adj(minChildIdx);
		}
		return;
	}
	//힙 삭제 연산 -> 삭제값 반환
	int del() {
		int res = minHeap[0];
		minHeap[0] = minHeap.back();
		minHeap.pop_back();
		del_adj(0);
		return res;
	}
	//empty 체크도함.
	int getMinValue() {
		return minHeap.empty() ? 0 : minHeap[0];
	}
};


int main() {
	int N;
	cin >> N;
	minHeap *minH = new minHeap();
	maxHeap *maxH = new maxHeap();
	int cmd;
	while (N--) {
		cin >> cmd;
		if (cmd == 0) {
			int positive = minH->getMinValue();
			int negative = maxH->getMaxValue();

			int res = 
				!positive && !negative ? 0 :
				!positive ? maxH->del() :
				!negative ? minH->del() :
				positive == -negative ? maxH->del() :
				positive > -negative ? maxH->del() : minH->del();
			cout << res << "\n";
		}
		else if (cmd < 0)
			maxH->push(cmd);
		else
			minH->push(cmd);
	}
}s