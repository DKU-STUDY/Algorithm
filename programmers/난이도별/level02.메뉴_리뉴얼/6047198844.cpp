#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <deque>
#include <list>

using namespace std;

//답을 반환한다.
//vec에는 조합 <문자열, 빈도수> 가 나오며 문자열은 크기 순대로 정렬되어있다.

vector<string> make_res(vector<pair<string, int>> vec, vector<int> course) {
    vector<string> res;
    //해당 오더에 해당하는 최대 값을 찾는다.
    for (int course_idx = 0; course_idx < course.size(); course_idx++) {
        int max_value = -1;
        for (int vec_idx = 0; vec_idx < vec.size(); vec_idx++) {
            if (vec[vec_idx].first.size() == course[course_idx]
                && vec[vec_idx].second > 1
                && (max_value == -1 || max_value == vec[vec_idx].second)) {
                if (max_value == -1)
                    max_value = vec[vec_idx].second;
                res.push_back(vec[vec_idx].first);
            }
        }
    }
    sort(res.begin(), res.end());
    return res;
}

void combi(string s, int remain, int idx, int end_idx, string &order, map <string, int>& combiCustomer) {
    if (remain == 0) {
        combiCustomer[s]++;
        return;
    }
    if (idx > end_idx)
        return;
    combi(s + order[idx], remain - 1, idx + 1, end_idx, order, combiCustomer);
    combi(s, remain, idx + 1, end_idx, order, combiCustomer);
}

//손님의 주문으로 만드는 모든 조합을 계산한다.
//길이 순으로 정렬한다.
map <string, int> makeCombi(vector<string> &orders) {
    map <string, int> combiCustomer;
    for (int i = 0; i < orders.size(); i++)
        for (int j = 2; j <= orders[i].size(); j++)
            combi("", j, 0, orders[i].size() - 1, orders[i], combiCustomer);
    return combiCustomer;
}

bool cmp(pair<string, int>& a, pair<string, int>& b) {
    //크기가 같을경우.
    if (a.first.size() == b.first.size())
        return a.second > b.second;
    return a.first.size() < b.first.size();
}

vector<string> solution(vector<string> orders, vector<int> course) {
    for (int i = 0; i < orders.size(); i++)
        sort(orders[i].begin(), orders[i].end());

    map <string, int> m = makeCombi(orders);
    vector<pair<string, int>> vec(m.begin(), m.end());
    sort(vec.begin(), vec.end(), cmp);
    return make_res(vec, course);
}

int main() {
    vector<string> s = solution({ "ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD" }, { 2, 3, 5 });
    cout << "\n";
}

//["AC", "ACDE", "BCFG", "CDE"]