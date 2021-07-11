#include <iostream>
#include <vector>
#include <math.h>
#include <climits>
using namespace std;

int N,num,Front,Back,ans = INT_MAX;
vector<int> v;
int ans_Front, ans_Back;

int main(void) {
	cin >> N;
	for(int i=0; i<N; i++) {
		cin >> num;
		v.push_back(num);
	}
	
	Front = 0;
	Back = N-1;
	
	while(Front<Back) { // 정렬된 상태라 크기의 순서를 보장하기 때문에 투 포인터를 사용했습니다. 
		if(abs(v[Front] + v[Back]) < abs(ans)) { // 최대한 0에만 가까우면 되기 때문에, 절댓값의 크기로 비교합니다. 
			ans_Front = v[Front];
			ans_Back = v[Back];	
			ans = abs(v[Front] + v[Back]);
		} 
		
		if(v[Front] + v[Back] < 0) Front++; // 0보다 작다면 앞을 가르키는 Front 포인터 ++ 
		else Back--; // 만약 0과 같거나 0보다 크다면 Back 포인터 -- 
	}
	cout << ans_Front << " " << ans_Back;
	return 0;
}
