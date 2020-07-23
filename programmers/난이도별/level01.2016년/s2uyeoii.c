#include <string>
#include <vector>

using namespace std;

string weeks[7] = { "FRI","SAT","SUN","MON","TUE","WED","THU"};
int month[12] = { 31,29,31,30,31,30,31,31,30,31,30,31 };

string solution(int a, int b) {
	string answer = "";
	int day = 0;
	for (int k = 0; k <(a-1); k++) {
		day += month[k];
	}
	day += (b-1);
	day %= 7;
	answer = weeks[day];

	return answer;
}
