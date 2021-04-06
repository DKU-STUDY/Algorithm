#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

vector<int> CompCoordinate(vector <int> Coord) {
	vector<int> Coord_ = Coord;
	sort(Coord_.begin(), Coord_.end());
	Coord_.erase(unique(Coord_.begin(), Coord_.end()), Coord_.end());
	map <int, int> m;
	for (int i = 0; i < Coord_.size(); i++)
		m[Coord_[i]] = i;
	for (int i = 0; i < Coord.size(); i++)
		Coord[i] = m[Coord[i]];
	return Coord;
}

int main() {
	int N;
	cin >> N;
	vector <int> Coord(N);
	for (int i = 0; i < N; i++)
		cin >> Coord[i];
	vector <int> CompCoord = CompCoordinate(Coord);
	for (int i : CompCoord)
		cout << i << " ";
}