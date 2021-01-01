#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <string>

using namespace std;

set <int> card;

int clock_num(int card_num) {
	vector <int> temp;
	for (int i = 0; i < 4; i++) {
		temp.push_back(card_num);
		card_num = card_num / 10 + (card_num % 10) * 1000;
	}
	return *min_element(temp.begin(), temp.end());
}

void make_card() {
	for (int card_num = 1111; card_num <= 9999; card_num++) {
		int n = card_num;
		while (n % 10)
			n = n / 10;
		if (n)
			continue;
		card.insert(clock_num(card_num));
	}
}

int main() {
	make_card();
	int res = 0;
	int num;
	for (int i = 1000; i > 0; i /= 10) {
		cin >> num;
		res += num * i;
	}
	vector <int> qwer;
	copy(card.begin(), card.end(), back_inserter(qwer));
	cout << find(qwer.begin(),qwer.end(),clock_num(res)) - qwer.begin() + 1;
}