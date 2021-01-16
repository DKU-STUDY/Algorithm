#include <iostream>
#include <queue>

using namespace std;

int check[2001];
bool flag[2001][2001];

int bfs(int S) {
	queue <pair<int, int>> q; // 상태, 클립보드에 저장된수
	q.push({1,0});
	int timer = 0;
	flag[1][0] = true;
	while (!q.empty()) {
		int q_size = q.size();
		while (q_size--) {
			//상태,클립보드
			pair <int, int> emoji = q.front();
			q.pop();
			if (emoji.first == S)
				return timer;
			//복사
			if (!flag[emoji.first][emoji.first]) {
				q.push({ emoji.first, emoji.first });
				flag[emoji.first][emoji.first] = true;
			}
			//붙여넣기
			if (emoji.first+emoji.second<=2000 && (!flag[emoji.first + emoji.second][emoji.second])) {
				q.push({emoji.first + emoji.second, emoji.second});
				flag[emoji.first + emoji.second][emoji.second] = true;
			}
			//삭제
			if (emoji.first > 0 && !flag[emoji.first - 1][emoji.second]) {
				q.push({ emoji.first - 1,emoji.second });
				flag[emoji.first - 1][emoji.second] = true;
			}
		}
		timer++;
	}
	return check[S];
}

int main() {
	int S;
	cin >> S;
	cout << bfs(S);
}