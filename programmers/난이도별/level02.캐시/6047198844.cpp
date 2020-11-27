#include <string>
#include <vector>
#include <unordered_map>
#include <list>

using namespace std;

int solution(int cacheSize, vector<string> cities) {
	if (!cacheSize)
		return cities.size()*5;

	int cities_size = cities.size();
	for (int i = 0; i < cities_size; i++) {
		int city_size = cities[i].size();
		for (int j = 0; j < city_size; j++) {
			if(cities[i][j]>='A'&& cities[i][j]<='Z')
				cities[i][j] = cities[i][j] - 'A' + 'a';
		}
	}

	unordered_map <string, list<string>::iterator> cache_map;
	list<string> cache;
	//가장 나중에 참조된것 --> 삭제한다.
	//cache에 있는것이 참조됨 --> 갱신한다.
	//cache의 맨앞에 있는것 --> 가장 최근에 참조된것 / cache의 맨뒤에 있는것 --> 가장 나중에 참조된것
	int time = 0;
	for (string city : cities) {
		//못찾았을경우
		if (cache_map.find(city) == cache_map.end()) {
			if (cache.size() == cacheSize) {
				string last = cache.back();
				cache_map.erase(last);
				cache.pop_back();
			}
			time += 5;
		}
		//찾았을경우
		else {
			cache.erase(cache_map[city]);
			time += 1;
		}
		cache.push_front(city);
		cache_map[city] = cache.begin();
	}
	return time;
}