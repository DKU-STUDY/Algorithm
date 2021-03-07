#include <vector>
#include <iostream>

using namespace std;

//삽입 조정
//기저 사례 : 부모가 없는 경우
//부모보다 큰경우 부모와 자신을 바꾼다.
void insert_adj(vector<int>& arr, int idx) {
	if (idx == 0)
		return;
	int parent_idx = (idx - 1) / 2;
	if (arr[parent_idx] < arr[idx]) {
		swap(arr[parent_idx], arr[idx]);
		insert_adj(arr, parent_idx);
	}
	return;
}

//삽입
//배열의 맨 끝에 원소를 삽입하고 조정한다.
void insert(vector<int>& arr, int element) {
	arr.push_back(element);
	insert_adj(arr, arr.size() - 1);
}
//삭제 조정
//기저 사례 : 자식의 인덱스가 끝 인덱스(N-1)보다 큰 경우
void del_adj(vector<int>& arr, int idx, int end_idx) {
	//자식이 둘다 없는 경우
	if (idx * 2 + 1 > end_idx)
		return;
	//자식이 하나인 경우
	if (idx * 2 + 1 == end_idx) {
		if (arr[idx * 2 + 1] > arr[idx])
			swap(arr[idx * 2 + 1], arr[idx]);
		return;
	}

	//자식이 둘인 경우
	//큰 자식 보다 작을경우.
	int big_idx = arr[idx * 2 + 1] < arr[idx * 2 + 2] ? idx * 2 + 2 : idx * 2 + 1;
	if (arr[idx] < arr[big_idx]) {
		swap(arr[idx], arr[big_idx]);
		del_adj(arr, big_idx, end_idx);
	}
	//자식 보다 클경우.
	return;
}

//삭제
//배열의 루트에 원소를 삽입하고 조정한다. 삭제한값을 반환한다.
int del(vector<int>& arr) {
	if (arr.empty())
		return 0;
	int res = arr[0];
	arr[0] = arr.back(); arr.pop_back();
	del_adj(arr, 0, arr.size() - 1);
	return res;
}

int main() {
	int N;
	scanf("%d", &N);
	vector<int>arr;
	int element;
	while (N--) {
		scanf("%d", &element);
		if (element)
			insert(arr, element);
		else
			printf("%d\n", del(arr));
	}
}