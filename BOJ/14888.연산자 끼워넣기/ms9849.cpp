#include <iostream>
#include <vector>
using namespace std;

vector<int> v;
int Cnt_op[4]; // 연산자 갯수를 저장하는 배열 
int N,num;
int Max=-1000000001, Min=1000000001;

void Recursion(int depth, int value) {
	int next_depth = depth+1; // depth+1
	int next_value; // 다음 재귀에 들어갈 값을 담는 변수 
	
	if(depth==N) {// 재귀 탈출 조건. 이 때 벡터에 0부터 입력받았으므로 depth가 N이면 v[N-1]까지의 연산을 완료한 것이다. 
		if(Max < value) Max = value;
		if(Min > value) Min = value; 
		return;
	}
	
	if(Cnt_op[0] != 0) { // + 연산자 
		Cnt_op[0]--;
		next_value = value + v[depth];
		Recursion(next_depth, next_value);
		Cnt_op[0]++;
	}
	if(Cnt_op[1] != 0) { // - 연산자 
		Cnt_op[1]--;
		next_value = value - v[depth];
		Recursion(next_depth, next_value);
		Cnt_op[1]++;
	}
	if(Cnt_op[2] != 0) { // * 연산자 
		Cnt_op[2]--;
		next_value = value * v[depth];
		Recursion(next_depth, next_value);
		Cnt_op[2]++;
	}
	if(Cnt_op[3] != 0) { // / 연산자  
		Cnt_op[3]--;
		next_value = value / v[depth];
		Recursion(next_depth, next_value);
		Cnt_op[3]++;
	}
}

int main(void) {
	cin >> N;
	for(int i=0; i<N; i++) {
		cin >> num;
		v.push_back(num);
	}
	
	for(int i=0; i<4; i++) cin >> Cnt_op[i];
	
	Recursion(1,v[0]); // 재귀를 이용하여 브루트 포스를 수행, 모든 값을 일일이 구해서 비교한다. 
	
	cout << Max << "\n" << Min; 
	return 0;
}
