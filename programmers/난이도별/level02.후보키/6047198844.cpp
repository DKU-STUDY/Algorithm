//map에 넣고 테스트
//후보키이면 1을 리턴
//아니면 끝에 도달할때까지
#include <vector>
#include <iostream>
#include <map>

using namespace std;

int rel_size;
vector <vector<int> > rel_col_t;
//idx : 현재 골라야하는 idx
//학번 이름 전공 학년
/*
	학번
	이름 전공
	이름 학년
	전공 학년
*/
//vt : 현재 뽑은 col
//rel_col_t : 해당 집합이 포함되서는 안된다.
int select_key(vector<vector<string>> &relation, vector <int> &vt, int idx, int current_sel, int target_sel) {
	if (current_sel == target_sel) {
		int rel_col_t_size = rel_col_t.size();
		int vt_size = vt.size();
		for (int i = 0; i < rel_col_t_size; i++) {
			int temp_size = rel_col_t[i].size();
			int cnt = 0;
			for (int j = 0; j < temp_size; j++) {
				for (int k = 0; k < vt_size; k++) {
					if (rel_col_t[i][j] == vt[k])
						cnt++;
				}
			}
			if (cnt == temp_size)
				return 0;
		}



		map <string, bool> mp;
		int relation_size = relation.size();
		vector<string> check_vt;
		for (int row = 0; row < relation_size; row++) {
			string temp;
			for (auto col : vt) {
				temp = temp + relation[row][col] + '/';
			}
			check_vt.push_back(temp);
		}
		int res = 1;
		int check_vt_size = check_vt.size();
		for (int i = 0; i < check_vt_size; i++) {
			if (mp.find(check_vt[i]) == mp.end()) {
				mp[check_vt[i]] = true;
			}
			else {
				res = 0;
				break;
			}
		}
		
		if (res) {
			vector <int> temp;
			for (auto col : vt)
				temp.push_back(col);
			rel_col_t.push_back(temp);
		}
		return res;
	}
	if (idx == rel_size)
		return 0;
	int answer = 0;
	for (int i = idx; i < rel_size; i++) {
		vt.push_back(i);
		answer += select_key(relation, vt, i + 1, current_sel + 1, target_sel);
		vt.pop_back();	
	}
	return answer;
}
int solution(vector<vector<string>> relation) {
	int answer = 0;
	vector <int> vt = {};
	rel_size = relation[0].size();
	for (int i = 1; i <= rel_size; i++) {
		answer += select_key(relation, vt, 0, 0, i);
	}
	return answer;

}
int main() {
	cout << solution({ {"100", "ryan", "music", "2"},
		              {"200", "apeach", "math", "1"},
		            {"300", "tube", "computer", "3"},
		             {"400", "con", "computer", "4"},
		               {"500", "muzi", "music", "3"},
		             {"600", "apeach", "music", "5"} });
}

/*
복습하기
#include <bits/stdc++.h>
 using namespace std;
bool possi(vector<int> &vec,int now){
	for(int i=0;i<vec.size();i++)
		if((vec[i]&now)==vec[i])return false;
	return true;
}
int solution(vector<vector<string>> relation) {
	int n=relation.size();
	int m=relation[0].size();
	vector<int> ans;
	for(int i=1;i<(1<<m);i++){
		set<string> s;
		for(int j=0;j<n;j++){
			string now="";
			for(int k=0;k<m;k++){
				if(i&(1<<k))now+=relation[j][k] + ' ';
			}
			s.insert(now);
		}
		if(s.size()==n&&possi(ans,i))ans.push_back(i);
	}
	return ans.size();
}

*/