/*
자음 / 모음으로 나눈다.
전체 - 자음갯수 = 모음갯수 인데, 모음갯수는 2와 같거나 커야한다.
전채 - 모음갯수 = 자음갯수
queue에 일단 넣고 정렬한다.


dfs로 구현
dfs(자음 갯수 , 모음 갯수)
*/
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <cstring>

using namespace std;

set <string> res_st;
vector <char> jaum;
vector <char> moum;

void dfs(int cnt_jaum, int cnt_total,bool blank[26],string res)
{
	if (!cnt_total){
		sort(res.begin(), res.end());
		res_st.insert(res); return;
	}

	if (cnt_jaum){
		for (int i = 0; i < moum.size(); i++) {
			if (!blank[moum[i] - 'a'])
			{
				blank[moum[i] - 'a'] = true;
				dfs(cnt_jaum - 1, cnt_total - 1, blank, res + moum[i]);
				blank[moum[i] - 'a'] = false;
			}
		}
	}
	else
	{
		int smallest = 0;
		if (!res.empty())
		{
			auto it = find(jaum.begin(), jaum.end(), res.back());
			if (it != jaum.end())
				smallest = it - jaum.begin();
		}

		for (int i = 0; i < jaum.size(); i++) {
			if (!blank[jaum[i] - 'a'])
			{
				blank[jaum[i] - 'a'] = true;
				dfs(cnt_jaum, cnt_total - 1, blank, res + jaum[i]);
				blank[jaum[i] - 'a'] = false;
			}
		}
	}
	return;
}

int main()
{
	int L, C;
	cin >> L >> C;
	char w;
	for (int i = 0; i < C; i++)
	{
		cin >> w;
		if (w == 'a' || w == 'e' || w == 'i' || w == 'o' || w == 'u')
			moum.push_back(w);
		else
			jaum.push_back(w);
	}
	sort(moum.begin(), moum.end());
	sort(jaum.begin(), jaum.end());

	int moum_size = moum.size();
	int moum_max_size = min(moum_size, (L - 2));
	for (int i = 1; i <= moum_max_size; i++)
	{
		string res = "";
		bool blank[26]; memset(blank, false, sizeof(bool) * 26);
		dfs(i, L, blank, res);
	}
		
	for (auto i = res_st.begin(); i != res_st.end(); i++)
		cout << *i << "\n";
}