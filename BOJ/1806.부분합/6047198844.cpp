//투포인터 이용.
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int main()
{
	int N; int S;
	vector <int> vt;
	cin >> N >> S;
	vt.resize(N);
	for (int i = 0; i < N; i++)
		cin >> vt[i];
	//투포인터는 양수에만 적용된다.
	//start는 현재합이 목표값보다 크거나 같은 경우 증가한다.
	//end 현재합이 목표값보다 작은 경우 증가한다.
	//start와 end가 같은 경우 현재합은 0이다.

	int part_sum = 0;
	int res = 100001;
	int end = 0;
	int start = 0;
	
	while(1)
	{
		if (part_sum >= S) {
			res = min(res, end - start);
			part_sum -= vt[start++];		
		}
		else if (end == N)
			break;
		else
			part_sum += vt[end++];
	}
	if (res != 100001)
		cout << res;
	else
		cout << 0;
}