#include <string>
#include <vector>
#include <cstring>
using namespace std;
//세로로 string 배열에 넣는다.
//우 , 하, 좌하를 check한다. size체크가 중요할듯.
//없앨것이 있다면 해당 주변을 먼저 체크한뒤 한번에 없앤다.
//없앨것이 없다면 (m*n) - string 배열 크기의 합을 반환한다.
int alpha_x[4] = { 0, 1,0,1 };
int alpha_y[4] = { 0, 0,1,1 };

int del_board(int m, int n, vector < string > &board) {
    //지우기 체크
    bool check_board[30][30];
    memset(check_board, false, sizeof(bool) * 30 * 30);
    bool check = false;
    for (int x = 0; x < n - 1; x++) {
        for (int y = 0; y < m - 1; y++) {
            bool equal_check = true;
            for (int i = 1; i < 4; i++)
                if (board[x][y]==' '||board[x][y] != board[x + alpha_x[i]][y + alpha_y[i]]) {
                    equal_check = false;
                    break;
                }
            if (equal_check) {
                check = true;
                for (int i = 0; i < 4; i++)
                    check_board[x + alpha_x[i]][y + alpha_y[i]] = true;
            }
                
        }
    }
    //지운것이 없다면 지운 누적값을 반환한다.
    if (!check) {
        int cnt = 0;
        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                if (board[x][y] == ' ')
                    cnt++;
            }
        }
        return cnt;
    }
    //내린다.
    //check_board의 true값을 모두 ' '으로 변환한다.
    for (int y = m - 1; y >= 0; y--)
        for (int x = 0; x < n; x++)
            if (board[x][y]!=' '&&check_board[x][y]) {
                board[x].erase(y, 1);
                board[x].push_back(' ');
            }

    return del_board(m, n, board);
}


int solution(int m, int n, vector<string> board) {
    int answer = 0;
    vector <string> col_board;
    for (int x = 0; x < n; x++) {
        string temp;
        for (int y = m - 1; y >= 0; y--) {
            temp += board[y][x];
        }
        col_board.push_back(temp);
    }

    answer = del_board(m, n, col_board);
    return answer;
}

int main() {
    solution(4, 5, { "AAAAA", "AUUUA", "AUUAA", "AAAAA" });
}