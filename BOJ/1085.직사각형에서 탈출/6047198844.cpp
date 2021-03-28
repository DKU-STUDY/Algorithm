#include <iostream>
#include <algorithm>

using namespace std;

int minDistance(int x, int y, int w, int h) {
	int yDiff = min(h - y, y);
	int xDiff = min(w - x, x);
	return min(yDiff, xDiff);
}

int main() {
	int x, y, w, h;
	cin >> x >> y >> w >> h;
	cout << minDistance(x, y, w, h);
}
