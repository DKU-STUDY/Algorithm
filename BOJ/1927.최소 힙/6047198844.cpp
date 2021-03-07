#include <iostream>
#include <vector>

using namespace std;

void insert_adj(vector<int> &heap,int child_idx) {
	if (child_idx == 0)
		return;
	int parent_idx = (child_idx - 1) / 2;
	if (heap[parent_idx] > heap[child_idx]) {
		swap(heap[parent_idx], heap[child_idx]);
		insert_adj(heap, parent_idx);
	}
	return;
}

void insert(vector<int> &heap, const int element) {
	heap.push_back(element);
	insert_adj(heap, heap.size() - 1);
}

void del_adj(vector<int> &heap, int parent,const int max_idx) {
	int leftChildIndex = parent * 2 + 1;
	int rightChildIndex = parent * 2 + 2;

	if (leftChildIndex > max_idx)
		return;
	
	int smallElementIndex = leftChildIndex;
	if (leftChildIndex != max_idx && heap[leftChildIndex] > heap[rightChildIndex])
		smallElementIndex = rightChildIndex;
	
	if (heap[smallElementIndex] < heap[parent]) {
		swap(heap[smallElementIndex], heap[parent]);
		del_adj(heap, smallElementIndex, max_idx);
	}

	return;
}

int del(vector<int> &heap) {
	if (heap.empty())
		return 0;
	int res = heap[0];
	heap[0] = heap.back(); heap.pop_back();
	del_adj(heap, 0, heap.size() - 1);

	return res;
}

int main() {
	int N;
	scanf("%d", &N);
	vector<int> heap;
	int cmd;
	while (N--) {
		scanf("%d", &cmd);
		if (cmd)
			insert(heap, cmd);
		else
			printf("%d\n",del(heap));
	}
}