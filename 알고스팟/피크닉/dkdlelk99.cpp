#include <iostream>
#include <vector> 
#include <memory.h>

using namespace std;
bool areFriend[10][10];
int n, m;

//쌍의 개수 (답)
int countPairs(vector<int>& relation)
{
	//짝이 없는 번호가 가장 빠른 학생 찾기
	int first = -1;
	for (int i = 0; i < n; i++)
	{
		if (!relation[i])
		{
			first = i;
			break;
		}
	}
	//기저 사례: 모든 학생이 짝을 찾음. 즉, 한가지 방법을 찾음
	if (first == -1) return 1;

	int ret = 0;
	for (int pairWith = first + 1; pairWith < n; pairWith++)
	{
		if (!relation[pairWith] && areFriend[first][pairWith])
		{
			relation[first] = relation[pairWith] = 1;
			ret += countPairs(relation);
			relation[first] = relation[pairWith] = 0;
		}
	}
	return ret;
}
int main()
{
	int testCase, r1, r2, answer;
	vector<int> relation;


	cin >> testCase;
	while (testCase--)
	{
		cin >> n >> m;
		relation = vector<int>(n, 0);
		memset(areFriend, 0, sizeof(areFriend));
		answer = 0;

		for (int i = 0; i < m; i++)
		{
			cin >> r1 >> r2;
			areFriend[r1][r2] = areFriend[r1][r2] = true;
		}
		answer = countPairs(relation);
		cout << answer <<endl;
	}
}
