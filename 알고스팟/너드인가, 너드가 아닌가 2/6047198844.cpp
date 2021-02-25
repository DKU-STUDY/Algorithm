#include <iostream>
#include <map>

using namespace std;

map <int, int> nerds;

//정복되었으면 true, 정복되지 않았으면 false를 반환한다.
bool isDonimated(int x, int y) {
	map <int, int>::iterator it = nerds.lower_bound(x);
	//맨오른쪽에 있는 경우는 항상 정복되지 않은 경우이다.
	if (nerds.end() == it) return false;

	//오른쪽에 값이 있는 경우. 오른쪽 값이 크다면(true) 정복된것이다.
	return y < it->second;
}

//기존 너드를 삭제한다.
//정복되지 않은 경우이다.
//x가 큰데, y가 작은 경우 삭제한다.
void removeNerds(int x, int y) {
	//it은 현재 x 오른쪽을 가리키고 있다.
	map <int, int>::iterator it = nerds.lower_bound(x);
	//왼쪽이 없으므로 . 삭제할것이 없다.
	//왼쪽만 삭제 가능하다. 오른쪽은 x가 크므로 , nerd이다.
	if (it == nerds.begin()) return;

	//왼쪽이 있는 경우이다. 현재 왼쪽을 가르킨다.
	--it;
	while (1) {
		//왼쪽이 점령당하지 않는 경우
		if (y < it->second) return;
		//끝에 도달한 경우
		if (it == nerds.begin()) {
			nerds.erase(it);
			return;
		}
		else {
			map <int, int>::iterator tit = it;
			--it;
			nerds.erase(tit);
			return;
		}
	}
}

//새로운 너드의 등록여부를 판단. 등록가능하면 기존 너드의 삭제가 가능할경우 삭제 후 등록, 등록불가능하면 등록하지 않고 기존의 크기 반환.
int registerNerds(int x, int y) {
	if (isDonimated(x, y)) return nerds.size();

	removeNerds(x, y);
	nerds[x] = y;
	return nerds.size();
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		int N;
		cin >> N;
		int result = 0;
		nerds.clear();
		while (N--) {
			int x, y;
			cin >> x >> y;
			result += registerNerds(x, y);
		}
		cout << result << "\n";
	}	
}