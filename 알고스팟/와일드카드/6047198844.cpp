#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

//memo[W][S]
//W ���� , S �־��� ���ڿ�
//res == -1 , �湮��������. res == 0 �ȵǴ� ��� res == 1 �Ǵ� ���.
bool dp(string& w, string& s,int w_idx,int s_idx,vector<vector<int> > &memo) {
	int& res = memo[w_idx][s_idx];
	if (res != -1)
		return res;

	int w_size = w.size();
	int s_size = s.size();

	while (w_idx < w_size && s_idx < s_size && (w[w_idx]==s[s_idx]||w[w_idx]=='?')) {
		w_idx++;
		s_idx++;
	}
	
	if (w_idx == w_size)
		return res = (s_idx == s_size);

	if (w[w_idx] == '*')
		for (int i = s_idx; i <= s_size; i++)
			if (dp(w, s, w_idx + 1, i, memo))
				return res = 1;

	return res = 0;
}l

//�� ���̽����� ����Ѵ�.

int main() {
	int C;
	cin >> C;
	string W;
	string S;
	int N;
	while (C--) {
		cin >> W;
		cin >> N;
		vector <string> res;
		while (N--) {
			cin >> S;
			vector <vector<int>> memo(W.size() + 1, vector<int>(S.size() + 1, -1));
			if (dp(W, S, 0, 0, memo))
				res.push_back(S);
		}
		sort(res.begin(), res.end());
		for (auto s : res)
			cout << s << "\n";
	}
}
