#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    stack <int> st[30];
    int row_size = board.size();
    int column_size = board[0].size();
    for (int x = 0; x < column_size; x++) {
        for (int y = row_size - 1; y >= 0; y--) {
            if (board[y][x])
                st[x].push(board[y][x]);
            else
                break;
        }
    }
    stack <int> res;
    int cnt = 0;
    for (int x : moves) {
        if (!st[x - 1].empty()) {
            int pick_num = st[x - 1].top();
            st[x - 1].pop();
            if (!res.empty() && res.top() == pick_num) {
                res.pop();
                cnt += 2;
            }
            else {
                res.push(pick_num);
            }
        }
    }
    return cnt;
}