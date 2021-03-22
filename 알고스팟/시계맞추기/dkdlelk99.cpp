#include <iostream>
#include <vector>
#include <algorithm>
#include <array>
using namespace std;

const int CLOCKS = 16, SWICHES = 10, INF = 9999;

// 연결된 스위치들 0~9
int swiches[10][5] = {
	{0, 1, 2, -1, -1}, {3, 7, 9, 11, -1}, {4, 10, 14, 15, -1},
	{0, 4, 5, 6, 7}, {6, 7, 8, 10, 12}, {0, 2, 14, 15, -1},
	{3, 14, 15, -1, -1}, {4, 5, 7, 14, 15},{1, 2, 3, 4, 5},
	{3, 4, 5, 9, 13}
};

//모든 시계가 12시를 가르키는지 검사
bool areAlined(vector<int> clocks)
{
	for (int i = 0; i < CLOCKS; i++)
		if (clocks[i] != 0) return false;
	return true;
}
//swich번 스위치를 누름
void push(vector<int>& clocks, int swich)
{
	int clock = -1, i = 0;
	for (i = 0; i < 5; i++)
	{
	  	if(swiches[swich][i] == -1) break;
		clock = swiches[swich][i];
		clocks[clock]++;
		if (clocks[clock] == 4) clocks[clock] = 0;
	}
}
int solve(vector<int>& clocks, int swich)
{
	if (clocks[8] != clocks[12]) return -1;
	else if (swich == SWICHES) return areAlined(clocks) ? 0 : INF;

	int ret = INF;
	for (int i = 0; i < 4; i++)
	{
		ret = min(ret, solve(clocks, swich + 1) + i);
		push(clocks, swich);
	}
	return ret;
}

int main()
{
	vector<int> clocks;
	int testCase, clock, answer;

	cin >> testCase;
	while (testCase--)
	{
		//시계 입력
		clocks.clear();
		for (int i = 0; i < 16; i++)
		{
			cin >> clock;
			if (clock == 12) clocks.push_back(0);
			else clocks.push_back(int(clock / 3));
		}

		answer = solve(clocks, 0);
		if (answer >= INF) cout << -1 << endl;
		else cout << answer << endl;
	}

	return 0;
}
