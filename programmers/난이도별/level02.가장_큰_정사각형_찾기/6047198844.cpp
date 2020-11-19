/*
완전탐색 방식 -> 시간 초과 -> 중복된 연산을 계속하고 있음 

#include <iostream>
#include<vector>
#include <algorithm>
using namespace std;

//정사각형인지 아닌지 탐험하는 함수
bool square(vector<vector<int>>& board, int y, int x, int size) {
    for (int check_y = y; check_y < y + size; check_y++) for (int check_x = x; check_x < x + size; check_x++)
        if (!board[check_y][check_x])
            return false;
    return true;
}

int solution(vector<vector<int>> board)
{
    int width = board[0].size();
    int height = board.size();

    int square_size = width > height ? height : width;
    while (square_size) {
        for (int y = 0; y <= height - square_size; y++)for (int x = 0; x <= width - square_size; x++) {
            if (square(board, y, x, square_size))
                return square_size * square_size;
        }
        --square_size;
    }
}*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int bottom_up(vector<vector<int>>& board, int y_range, int x_range) {
    int memo[1000][1000];
    memset(memo, 0, 1000 * 1000);
    // width (0,x_range) height (0,y_range)
    for (int y = 0; y <= y_range; y++) for (int x = 0; x <= x_range; x++) {
        if (!board[y][x])
            memo[y][x] = 0;
        else {
            if (y-1 >= 0 && x-1 >= 0) {
                memo[y][x] = min(min(memo[y - 1][x], memo[y - 1][x - 1]), memo[y][x - 1]) + 1;
            }
            else {
                memo[y][x] = 1;
            }
        }
    }
    int answer = 0;
    for (int y = 0; y <= y_range; y++) for (int x = 0; x <= x_range; x++)
        if (answer < memo[y][x])
            answer = memo[y][x];
    return answer * answer;
}

int solution(vector<vector<int> > board) {
    int width = board[0].size() - 1;
    int height = board.size() - 1;
    return bottom_up(board, height, width);
}