/*
강호는 코딩 교육을 하는 스타트업 스타트링크에 지원했다. 
오늘은 강호의 면접날이다. 
하지만, 늦잠을 잔 강호는 스타트링크가 있는 건물에 늦게 도착하고 말았다.

스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 
스타트링크가 있는 곳의 위치는 G층이다. 강호가 지금 있는 곳은 S층이고, 
이제 엘리베이터를 타고 G층으로 이동하려고 한다.

보통 엘리베이터에는 어떤 층으로 이동할 수 있는 버튼이 있지만, 
강호가 탄 엘리베이터는 버튼이 2개밖에 없다. 
U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼이다. 
(만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)

강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성하시오. 
만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력한다.


base case
	queue에 값이 없는 경우 -> use the stairs
	G에 도착한 경우 -> 횟수 출력
특정 층 도착 -> 방문처리
완전탐색으로 풀수있는가?
10! = 약 300만. 300만을 넘지 않는다. 최고 층수가 100만이므로.
*/

#include <iostream>
#include <queue>

using namespace std;

bool check[1000001];

int brute_force_bfs(int F, int S, int G, int U, int D)
{
	int res = 0;
	if (S == G)
		return res;

	queue <int> q; q.push(S); check[S] = true;

	while (!q.empty())
	{
		++res;
		int size = q.size();
		while (size--)
		{
			int current_floor = q.front(); q.pop();
			int up_stairs = current_floor + U;
			int down_stairs = current_floor - D;

			if ((up_stairs == G) || (down_stairs == G))
				return res;


			if ((up_stairs <= F)&&!check[up_stairs]){
                q.push(up_stairs); check[up_stairs] = true;
            }
				
			if (down_stairs >= 1 && !check[down_stairs]){
               q.push(down_stairs); check[down_stairs] = true;
            }
				
		}
	}
	return -1;
}
int main()
{
	//총 F층
	//스타트링크가 있는 위치 G층 
	// 강호가 있는 층 S층 
	// U버튼 위로 U층을 가는 버튼 
	// D버튼 아래로 D층을 가는버튼
	
	int F, S, G, U, D;
	cin >> F >> S >> G >> U >> D;
	int res;
	res = brute_force_bfs(F, S, G, U, D);
	if (res>=0)
		cout << res;
	else
		cout << "use the stairs";
}
