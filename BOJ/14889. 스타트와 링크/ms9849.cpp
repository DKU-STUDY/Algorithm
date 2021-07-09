#include <iostream>
#include <math.h>
using namespace std;

int N;
int arr[21][21];
int checked[21];
int Min=100000000;

void Recursion(int match,int depth) {
	int next_depth = depth+1;
	
	if(depth == N/2) {
		int comp1=0,comp2=0,ans;
		for(int i=1; i<=N; i++) {
			for(int j=1; j<=N; j++) {
				if(checked[i]==0 && checked[j]==0)  // 한 팀에 있는 사람들끼리의 arr값을 합침 
					comp1+= arr[i][j];	
				else if(checked[i]==1 && checked[j]==1) // 나머지 팀에 있는 사람들끼리 arr 값을 합침 
					comp2+= arr[i][j];		
			}	
		} 
		ans = abs(comp1-comp2);
		if(Min > ans) Min = ans;
		return;
	}
	
	for(int i=match+1; i<N; i++) {
		if(!checked[i]) {
			checked[i] = 1;
			Recursion(i, next_depth);
			checked[i] = 0;
		}
	}
}


int main(void) {
	cin >> N;
	
	for(int i=1; i<=N; i++)
		for(int j=1; j<=N; j++)
			cin >> arr[i][j];
	
	for(int i=1; i<=N; i++) {
		checked[i] = 1;
		Recursion(i,1);
		checked[i] = 0;
	}
	
	cout << Min;
	return 0;
}
